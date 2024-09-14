import pytest
from string_utils import StringUtils

utils = StringUtils()

'''capitalize'''

def test_capitalize() :
    """POSITIVE"""
    assert utils.capitalize("skypro")== "Skypro"
    assert utils.capitalize("hello")== "Hello"
    assert utils.capitalize("123")== "123"
    """NEGATIVE"""
    assert utils.capitalize("")== ""
    assert utils.capitalize(" ")== " "
    assert utils.capitalize("12345тест")== "12345тест"

@pytest.mark.parametrize("input_string, exected_output", [
    ("skypro", "Skypro"),
    ("hello", "Hello"),
    ("123", "123"),
    ('', ""),
    (' ', " "),
    ("12345тест", "12345тест"),
])
def test_capitalize(input_string, exected_output):
    assert utils.capitalize(input_string) == exected_output

    """trim"""

    
    def test_trim():
        """POSITIVE"""
        assert utils.trim(" skypro") == "skypro" 
        assert utils.trim(" hello") == "hello"
        assert utils.trim(" SKY ") == "SKY " 
        """NEGATIVE"""
        assert utils.trim("") == ""

@pytest.mark.xfail()
def test_trim_with_numbers_input():
    assert utils.trim(12345) == "12345"

 
@pytest.mark.xfail()
def test_trim_with_spaces_output():
    assert utils.trim(" SKY ") == " SKY "  

    """to_list"""

@pytest.mark.parametrize('string, delimeter, result', [
   # POSITIVE
   ("яблоко,банан,апельсин", ",", ["яблоко", "банан", "апельсин"]),
   ("1,2,3,4,5", ",", ["1", "2", "3", "4", "5"]),
   ("*@$@%@&", "@", ["*", "$", "%", "&" ]),
   # NEGATIVE
   ("", None, []),
   ("1,2,3,4,5", None, ["1", "2", "3", "4 5"]),
])
def test_to_List(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else: 
        res = utils.to_list(string,delimeter)
    assert res == result 
    
    
    """contains"""

@pytest.mark.parametrize('string, symbol, result', [
    ("банан", "б", True),
    (" гвоздь", "д", True),
    ("мир ", "р",True),
    ("диван-кровать", "-", True),
    ("145", "1", True),
    ("", "", True),
    ("Москва","м", False),
    ("привет", "з", False), 
    ("кот", "№", False),
    ("", "з", False),
    ("12345", "h", False),
    # ("hello", "", False) # Ошибка,система не корректно работает со строкой,которая не содержит ни одного символа

])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result

    """delete_symbol"""

@pytest.mark.parametrize('string, symbol, result', [
    ("шапка", "ш", "апка"),
    ("Анюта", "т", "Анюа"),
    ("123", "1", "23"),
    ("Тель Авив", " ", "ТельАвив"),
    
    ("", "", ""),
    ("", "с", ""),
    ("море", "", "море"),
    ("чайки", " ", "чайки"),
])
def test_delete_symbol(string, symbol, result):
    res = utils.dalete_symbol(string, symbol)
    assert res == result

    """starts_with"""

@pytest.mark.parametrize('string, symbol, result', [

    ("пляж", "п", True),
    ("", "", True),
    ("Афины", "A", True),
    ("Film ",  "F", True),
    ("Коста-Рика", "К", True),
    ("123", "1", True),

    ("Оля", "о", False),
    ("кино", "К", False),
    ("", "@", False),
    ("машина", "г", False),
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result

    """end_with"""

@pytest.mark.parametrize('string, symbol, result', [
    ("Толя", "я", True),
    ("МИР", "Р", True),
    ("", "", True),
    ("кот ","", True),
    ("123", "3", True),

    ("сено", "р", False),
    ("", "*", False),
])
def test_end_with(string, symbol, result): 
    res = utils.end_with(string, symbol)
    assert res == result

    """is_empty"""

@pytest.mark.parametrize('string, result',[
    ("", True),
    (' ', True),
    ("  ", True),

    ("не пусто", False),
    (" не пусто с пробелом", False),
    ("123", False),
])
def test_is_empty(string, result): 
     res = utils.is_empty(string)
     assert res == result

     """list_to_string"""


@pytest.mark.parametrize('lst, joiner, result', [
    (["s", "o","s"], ",", "s,o,s"),
    ([1,2,3,4,5], None, "1,2,3,4,5"),
    (["Первый", "Второй"], "-", "Первый-Второй"),
    (["Первый", "Второй"], "Середина", "ПервыйСерединаВторой"),

    ([], None, ""),
    ([], ",", ""),
    ([], "кот", "")
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(Ist)
    else: 
        res = utils.list_to_string(Ist, joiner)  
    assert res == result


                           