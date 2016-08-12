"""
Defines the core objects for ePinXtractr.
"""
from collections import namedtuple



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
