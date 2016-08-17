"""
Defines the core objects for ePinXtractr.
"""
import sys
import json
import shutil
import os.path
import xml.etree.ElementTree as ET
from datetime import datetime
from collections import namedtuple

from dolfin import Storage as _ 



class EPin(namedtuple('EPin', 'number, value')):
    """Represents the details for a single electronic-pin for mobile airtime."""
    
    PIN_LENGTH = 16

    def __new__(cls, number, value):
        if not EPin.is_valid_number(number):
            raise ValueError("Invalid ePin number: %s" % number)
        if not EPin.is_valid_value(value):
            raise ValueError("Invalid ePin value: %s" % value)
        return super(EPin, cls).__new__(cls, number, value)
    
    @staticmethod
    def is_valid_number(value):
        if value and len(value) == EPin.PIN_LENGTH:
            invalid = [d for d in value if not d.isdigit()]
            return len(invalid) == 0
        return False
    
    @staticmethod
    def is_valid_value(value):
        if value:
            try:
                value = int(value)
                return value > 0 and value % 100 == 0
            except:
                pass
        return False


class Packt(namedtuple('Packt', 'pins, value, quantity')):
    """Represents a collection of epins all of the same airtime value collected 
    together in a single sms message body. 
    """

    FIELD_LABELS = ("PIN(S)", "VALUE", "QTY")

    @property
    def count(self):
        return len(self.pins) if self.pins else 0
    
    def __iter__(self):
        for pin in self.pins:
            yield EPin(pin, self.value)

    @staticmethod
    def parse(message):
        message = (message or "").upper()
        indexes = [message.find(x + ':') for x in Packt.FIELD_LABELS]

        if not message or -1 in indexes:
            raise ValueError("Message format is invalid.")
        
        record = message[indexes[0] : message.find(' ', indexes[-1])]
        fields = record.strip().split(' ')
        if not fields or len(fields) != 3:
            raise ValueError("Record format in message is invalid.")
        
        args = []
        for i, label in enumerate(Packt.FIELD_LABELS):
            parts = fields[i].split(':')
            if not parts or len(parts) != 2 or parts[0] != label:
                raise ValueError("Record format in message is invalid.")
            
            field_value = parts[1]
            if i == 0:
                pins = tuple([x for x in field_value.split(',') if x])
                args.append(pins)
            else:
                try:
                    value = int(field_value)
                    args.append(value)
                except:
                    raise Value("Record field value is invalid: %s" % parts[0])
        
        return Packt(*args)


class SNGen(object):
    """Represents a serial number generator of some sort which embeds a time
    stamp at the start of generated number sequences. The numbers that follow
    the timestamp are sequence and begin at indicated offset.
    """

    MIN_SERIAL_LENGTH = 14
    TIMESTAMP_LENGTH  = 12
    TIMESTAMP_FORMAT  = '%y%m%d%H%M%S'

    def __init__(self, timestamp=None, offset=1, length=20):
        if length < self.MIN_SERIAL_LENGTH:
            fmt = "Generated sequence length must be {} or more."
            raise ValueError(fmt.format(self.MIN_SERIAL_LENGTH))

        self.timestamp = (timestamp or datetime.now())
        self._offset = offset or 1
        self._length = length
        self._current = None
        self._counter = 0
        self._gen = None
    
    @property
    def current(self):
        if not self._current:
            return self.get()
        return self._current
    
    def get(self):
        return next(self.__iter__())
    
    def __iter__(self):
        if not self._gen:
            self._gen = self.__make_iterator()
        return self._gen
    
    def __make_iterator(self):
        tstamp_str = self.timestamp.strftime(self.TIMESTAMP_FORMAT)
        pad_length = self._length - self.TIMESTAMP_LENGTH
        sn_format = '{}{:0>%s}' % pad_length
        
        while True:
            self._current = sn_format.format(
                tstamp_str, self._offset + self._counter)
            yield self._current
            self._counter += 1


class HallowIndicator(object):
    """Represents a 'hallow' progress indicator which basically sinks all
    initiated method calls.
    """
    
    def init(self, task_count=0, level=0):
        pass
    
    def update(self, done=False, task_passed=None):
        pass


class EPXEngine(object):

    EPIN_LINE_FORMAT = "{number},{serial},{value},00000,{today}"
    REPORT_FILENAME = 'result.html'
    EPINS_FILENAME = 'epins.txt'

    def __init__(self, target_ext='.xml'):
        self._target_ext = (target_ext or '.xml')
        self.__sngen = None
    
    @property
    def sngen(self):
        if not self.__sngen:
            self.__sngen = SNGen()
        return self.__sngen
    
    @sngen.setter
    def sngen(self, value):
        self.__sngen = value

    def parse(self, smsfile):
        if isinstance(smsfile, str):
            if not os.path.exists(smsfile):
                raise FileNotFoundError(smsfile)
        
        root = ET.parse(smsfile).getroot()
        for node in root.findall('./sms'):
            yield Packt.parse(node.attrib['body'])
    
    def process(self, dirpath, indicator=None):
        if not os.path.exists(dirpath):
            raise ValueError("Provided directory path doesn't exist.")
        
        # remove target files
        for name in [self.EPINS_FILENAME, self.REPORT_FILENAME]:
            try:
                fullpath = os.path.join(dirpath, name)
                if os.path.exists(fullpath):
                    os.remove(fullpath)
            except:
                pass
            
        result = _(dirpath=dirpath, errors=[], failed=[], passed=[], lines=[])
        pInd = (indicator or HallowIndicator())
        try:
            filenames = self._listdir(dirpath)
            pInd.init(task_count=len(filenames), level=0)
        except Exception as ex:
            result.errors.append(_(filename=None, smsno=None, error=str(ex)))
        else:
            first_flush = True
            for f in filenames:
                passed = self._process_file(f, result)
                pInd.update(done=False, task_passed=passed)
                if len(result.lines) >= 1000:
                    self._flush_result(result, first_flush)
                    first_flush=False
            self._flush_result(result, first_flush)
            pInd.update(done=True)
        return result
    
    def write_report(self, result):
        fullpath = os.path.join(result.dirpath, self.REPORT_FILENAME)
        with open(fullpath, 'w') as f:
            json.dump(result, f, indent=4)
            f.flush()
    
    def _format_epin(self, epin):
        line = self.EPIN_LINE_FORMAT\
                   .replace('{number}', epin.number)\
                   .replace('{serial}', self.sngen.get())\
                   .replace('{value}', '{:0>7}00'.format(epin.value))\
                   .replace('{today}', self.sngen.timestamp.strftime('%d/%m/%Y'))
        return line
    
    def _flush_result(self, result, first_flush):
        dirpath = result.dirpath
        if result.lines:
            fullpath = os.path.join(dirpath, self.EPINS_FILENAME)
            with open(fullpath, 'w' if first_flush else 'a') as f:
                f.write('\n'.join(result.lines))
                f.flush()
            result.lines = []
        
        for label in ["passed"]:
            if result[label]:
                dirdest = os.path.join(dirpath, "_%s" % label)
                self._move_files(result[label], dirpath, dirdest, result)

    def _process_file(self, filename, result):
        dirpath, passed = (result.dirpath, False)
        try:
            lines, smsno = ([], 1)
            for packt in self.parse(os.path.join(dirpath, filename)):
                for epin in packt:
                    lines.append(self._format_epin(epin))
                smsno += 1
            
            result.passed.append(filename)
            result.lines.extend(lines)
            passed = True
        except Exception as ex:
            result.errors.append(_(filename=filename, smsno=smsno, error=str(ex)))
            result.failed.append(filename)
            passed = False
        return passed
    
    def _listdir(self, dirpath):
        if not dirpath or not os.path.isdir(dirpath):
            raise ValueError('Invalid directory path provided.')
        
        filenames = []
        for f in os.listdir(dirpath):
            if self._target_ext:
                if not f.endswith(self._target_ext):
                    continue
            filenames.append(f)
        return filenames
    
    def _move_files(self, files, dirpath, dirdest, result):
        if not os.path.exists(dirdest):
            try:
                os.mkdir(dirdest)
            except Exception as ex:
                err_msg = "Unabled to create directory. (Error: %s)"
                result.errors.flush.append(err_msg % str(ex))
        
        if files and os.path.exists(dirdest):
            for f in files:
                try:
                    shutil.move(os.path.join(dirpath, f), dirdest)
                except Exception as ex:
                    err_msg = "Unable to move file. (Error: %s)"
                    result.errors.flush.append(err_msg % str(ex))
    