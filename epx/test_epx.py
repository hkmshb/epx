import pytest
import os.path
from datetime import datetime
from epx.core import EPin, Packt, SNGen, EPXEngine



FIXTURE_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')


@pytest.fixture
def epin():
    return EPin(number='6673347746062497', value=100)


@pytest.fixture
def packt():
    message = (
        "Msg:ERC PIN(s):6673347746062494,6159625120254922,6186892456912475,"
        "6220427192339577,6738008238122646, Value:100 Qty:5 To recharge Dial"
        " *126*PIN# for voice or *143*PIN# for data &amp; press OK")
    return Packt.parse(message)


@pytest.fixture
def smsfile():
    filename = os.path.join(FIXTURE_DIR, 'sample-smsbackup.xml')
    return open(filename, 'r')


class TestEPin(object):

    def test_construction(self):
        epin = EPin(number='6673347746062494', value=100)
        assert epin != None
    
    def test_creation_fails_if_number_not_all_digits(self):
        with pytest.raises(ValueError):
            EPin(number='667334774606249A', value=200)
    
    def test_creation_fails_if_value_isnot_integer(self):
        with pytest.raises(ValueError):
            EPin(number='6673347746062494', value='10A')
    
    def test_creation_fails_if_number_length_not_16(self):
        # test with 15-digit number
        with pytest.raises(ValueError):
            EPin(number='667334774606249', value=100)

    def test_creation_fails_for_value_not_gt_zero_and_multiple_of_100(self):
        with pytest.raises(ValueError):
            EPin(number='6673347746062494', value=105)

    def test_is_immutable(self, epin):
        with pytest.raises(AttributeError):
            epin.value = 700
        
        with pytest.raises(AttributeError):
            epin.number = '777'


class TestPackt(object):

    def test_can_parse_epin_info_from_message_body(self):
        message = (
            "Msg:ERC PIN(s):6673347746062494,6159625120254922,6186892456912475,"
            "6220427192339577,6738008238122646, Value:100 Qty:5 To recharge Dial"
            " *126*PIN# for voice or *143*PIN# for data &amp; press OK")
        packt = Packt.parse(message)
        assert packt != None
    
    def test_is_immutable(self, packt):
        with pytest.raises(AttributeError):
            packt.pins = ('12345','67890')
    
    def test_is_iteratable(self, packt):
        count = 0
        for epin in packt:
            assert isinstance(epin, EPin)
            count += 1
        assert packt.count == count


class TestSNGen(object):
    sngen = SNGen()

    def test_default_serial_startswith_default_timestamp_of_today(self):
        serial = self.sngen.current
        assert serial.startswith(datetime.now().strftime('%y%m%d%H'))
    
    def test_default_first_serial_endswith_default_offset(self):
        serial = self.sngen.current
        assert serial.endswith('1')
    
    def test_default_serial_has_length_of_20(self):
        serial = self.sngen.current
        assert len(serial) == 20
    
    def test_custom_serial_startswith_specified_timestamp(self):
        custom_datetime = datetime(2010, 1, 1, 13, 34)
        serial = SNGen(custom_datetime).current
        assert serial.startswith(custom_datetime.strftime('%y%m%d%H'))
    
    def test_custom_first_serial_endswith_specified_offset(self):
        offset = 2345
        serial = SNGen(offset=offset).current
        assert serial.endswith(str(offset))
    
    def test_custom_serial_length_match_specified_length(self):
        serial_length = 17
        serial = SNGen(length=serial_length).current
        assert len(serial) == serial_length
    
    def test_creation_fails_for_length_less_than_MIN_SERIAL_LENGTH(self):
        with pytest.raises(ValueError):
            SNGen(length=SNGen.MIN_SERIAL_LENGTH - 1)


class TestEXPEngine(object):
    engine = EPXEngine()

    def test_nneds_existing_dirpath_to_process(self):
        with pytest.raises(ValueError):
            result = self.engine.process(r'c:\fake-dir')
    
    def test_parse_returns_an_iterator(self, smsfile):
        iterobj = self.engine.parse(smsfile)
        assert hasattr(iterobj, '__iter__') == True
    
    def test_parse_iterator_item_is_packt_object(self, smsfile):
        iterobj = self.engine.parse(smsfile)
        packt = iterobj.__next__()
        assert isinstance(packt, Packt) == True
        assert packt.quantity == packt.count
        assert packt.quantity == 5
    
    def test_epin_format_output_has_5fields_delimited_by_comma(self, epin):
        line = self.engine._format_epin(epin)
        assert line and ',' in line
        assert len(line.split(',')) == 5
    
    def test_epin_format_output_has_pin_number_field(self, epin):
        line = self.engine._format_epin(epin)
        assert len(epin.number) == 16 and line.startswith(epin.number)
    
    def test_epin_format_output_has_serial_field(self, epin):
        line = self.engine._format_epin(epin)
        serial = self.engine.sngen.current
        assert len(serial) == 20 and serial in line
        assert line.split(',')[1] == serial
    
    def test_epin_format_output_has_pin_value_field(self, epin):
        line = self.engine._format_epin(epin)
        assert str(epin.value) in line
        
        value_field = line.split(',')[2]
        assert len(value_field) == 9 and str(epin.value) in value_field
        assert value_field == '{:0>7}00'.format(epin.value)
    
    def test_epin_format_output_has_dummy_five_zeros_field(self, epin):
        five_zeros, line = '00000', self.engine._format_epin(epin)
        assert five_zeros in line
        assert line.split(',')[3] == five_zeros

    def test_epin_format_output_has_date_field(self, epin):
        today = self.engine.sngen.timestamp.strftime('%d/%m/%Y')
        line = self.engine._format_epin(epin)
        assert line.endswith(today)
