import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# Делает первую букву заглавной
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Удаляет пробел в начале
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    (" hello world", "hello world"),
    ("         python", "python"),
])
def test_trim_positive(input_str, expected):  
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("skypro", "skypro"),
    ("   ","")])
def test_trim_negative(input_str, expected):  
    assert string_utils.trim(input_str) == expected

#Поиск искомого символа
@pytest.mark.positive
@pytest.mark.parametrize("input_str,simbol", [
    ("SkyPro", "S"),
    ("hello world", "h"),
    (" ", " "),
])
def test_contains_positive(input_str, simbol):  
    assert string_utils.contains(input_str,simbol) == True

@pytest.mark.negative
@pytest.mark.parametrize("input_str, simbol", [
    ("", " "),
    ("skypro", "A"),
    ("python"," ")])
def test_contains_negative(input_str, simbol):  
    assert string_utils.contains(input_str,simbol) == False

# Удаление символа
@pytest.mark.positive
@pytest.mark.parametrize("input_str,simbol", [
    ("SkyPro", "S"),
    ("hello world", "h"),
    ("  ", " "),
])
def test_delete_symbol_positive(input_str, simbol):  
    assert string_utils.delete_symbol(input_str,simbol) 

@pytest.mark.negative
@pytest.mark.parametrize("input_str, simbol", [
    ("", " "),
    ("skypro", "A"),
    ("python"," ")])
def test_delete_symbol_negative(input_str, simbol):  
    assert string_utils.delete_symbol(input_str,simbol) 
