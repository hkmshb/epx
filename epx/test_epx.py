import pytest
from epx.core import EPin, Packt



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
