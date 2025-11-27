import pytest
from string_utils import StringUtils

# Инициализация объекта для тестирования
@pytest.fixture
def string_utils():
    return StringUtils()

# Тесты для capitilize
class TestCapitilize:
    def test_capitilize_positive(self, string_utils):
        """Позитивный тест: строка с маленькой буквы"""
        result = string_utils.capitilize("skypro")
        assert result == "Skypro"

    def test_capitilize_empty_string(self, string_utils):
        """Негативный тест: пустая строка"""
        result = string_utils.capitilize("")
        assert result == ""

    def test_capitilize_already_capitalized(self, string_utils):
        """Позитивный тест: строка уже с большой буквы"""
        result = string_utils.capitilize("Skypro")
        assert result == "Skypro"

    def test_capitilize_with_numbers(self, string_utils):
        """Позитивный тест: строка с числами"""
        result = string_utils.capitilize("123 test")
        assert result == "123 test"

# Тесты для trim
class TestTrim:
    def test_trim_positive(self, string_utils):
        """Позитивный тест: строка с пробелами в начале"""
        result = string_utils.trim("   skypro")
        assert result == "skypro"

    def test_trim_multiple_spaces(self, string_utils):
        """Позитивный тест: много пробелов в начале"""
        result = string_utils.trim("     skypro")
        assert result == "skypro"

    def test_trim_no_spaces(self, string_utils):
        """Позитивный тест: строка без пробелов в начале"""
        result = string_utils.trim("skypro")
        assert result == "skypro"

    def test_trim_empty_string(self, string_utils):
        """Негативный тест: пустая строка"""
        result = string_utils.trim("")
        assert result == ""

    def test_trim_only_spaces(self, string_utils):
        """Негативный тест: строка только из пробелов"""
        result = string_utils.trim("   ")
        assert result == ""

# Тесты для to_list
class TestToList:
    def test_to_list_default_delimiter(self, string_utils):
        """Позитивный тест: разделитель по умолчанию"""
        result = string_utils.to_list("a,b,c,d")
        assert result == ["a", "b", "c", "d"]

    def test_to_list_custom_delimiter(self, string_utils):
        """Позитивный тест: кастомный разделитель"""
        result = string_utils.to_list("1:2:3", ":")
        assert result == ["1", "2", "3"]

    def test_to_list_empty_string(self, string_utils):
        """Негативный тест: пустая строка"""
        result = string_utils.to_list("")
        assert result == []

    def test_to_list_single_item(self, string_utils):
        """Позитивный тест: один элемент"""
        result = string_utils.to_list("hello")
        assert result == ["hello"]

    def test_to_list_with_spaces(self, string_utils):
        """Позитивный тест: строка с пробелами"""
        result = string_utils.to_list("a, b, c")
        assert result == ["a", " b", " c"]

# Тесты для contains
class TestContains:
    def test_contains_positive(self, string_utils):
        """Позитивный тест: символ присутствует"""
        result = string_utils.contains("SkyPro", "S")
        assert result == True

    def test_contains_negative(self, string_utils):
        """Негативный тест: символ отсутствует"""
        result = string_utils.contains("SkyPro", "U")
        assert result == False

    def test_contains_empty_string(self, string_utils):
        """Негативный тест: пустая строка"""
        result = string_utils.contains("", "a")
        assert result == False

    def test_contains_empty_symbol(self, string_utils):
        """Негативный тест: пустой символ"""
        result = string_utils.contains("test", "")
        assert result == True

# Тесты для delete_symbol
class TestDeleteSymbol:
    def test_delete_symbol_single_char(self, string_utils):
        """Позитивный тест: удаление одного символа"""
        result = string_utils.delete_symbol("SkyPro", "k")
        assert result == "SyPro"

    def test_delete_symbol_substring(self, string_utils):
        """Позитивный тест: удаление подстроки"""
        result = string_utils.delete_symbol("SkyPro", "Pro")
        assert result == "Sky"

    def test_delete_symbol_nonexistent(self, string_utils):
        """Негативный тест: удаление несуществующего символа"""
        result = string_utils.delete_symbol("SkyPro", "X")
        assert result == "SkyPro"

    def test_delete_symbol_empty_string(self, string_utils):
        """Негативный тест: пустая строка"""
        result = string_utils.delete_symbol("", "a")
        assert result == ""

# Тесты для starts_with
class TestStartsWith:
    def test_starts_with_positive(self, string_utils):
        """Позитивный тест: начинается с символа"""
        result = string_utils.starts_with("SkyPro", "S")
        assert result == True

    def test_starts_with_negative(self, string_utils):
        """Негативный тест: не начинается с символа"""
        result = string_utils.starts_with("SkyPro", "P")
        assert result == False

    def test_starts_with_empty_string(self, string_utils):
        """Негативный тест: пустая строка"""
        result = string_utils.starts_with("", "S")
        assert result == False

    def test_starts_with_empty_symbol(self, string_utils):
        """Негативный тест: пустой символ"""
        result = string_utils.starts_with("test", "")
        assert result == True

# Тесты для end_with
class TestEndWith:
    def test_end_with_positive(self, string_utils):
        """Позитивный тест: заканчивается символом"""
        result = string_utils.end_with("SkyPro", "o")
        assert result == True

    def test_end_with_negative(self, string_utils):
        """Негативный тест: не заканчивается символом"""
        result = string_utils.end_with("SkyPro", "y")
        assert result == False

    def test_end_with_empty_string(self, string_utils):
        """Негативный тест: пустая строка"""
        result = string_utils.end_with("", "o")
        assert result == False

    def test_end_with_empty_symbol(self, string_utils):
        """Негативный тест: пустой символ"""
        result = string_utils.end_with("test", "")
        assert result == True

# Тесты для is_empty
class TestIsEmpty:
    def test_is_empty_positive(self, string_utils):
        """Позитивный тест: пустая строка"""
        result = string_utils.is_empty("")
        assert result == True

    def test_is_empty_only_spaces(self, string_utils):
        """Позитивный тест: только пробелы"""
        result = string_utils.is_empty("   ")
        assert result == True

    def test_is_empty_negative(self, string_utils):
        """Негативный тест: не пустая строка"""
        result = string_utils.is_empty("SkyPro")
        assert result == False

    def test_is_empty_with_spaces(self, string_utils):
        """Позитивный тест: строка с пробелами"""
        result = string_utils.is_empty("  test  ")
        assert result == False

# Тесты для list_to_string
class TestListToString:
    def test_list_to_string_default_joiner(self, string_utils):
        """Позитивный тест: разделитель по умолчанию"""
        result = string_utils.list_to_string([1, 2, 3, 4])
        assert result == "1, 2, 3, 4"

    def test_list_to_string_custom_joiner(self, string_utils):
        """Позитивный тест: кастомный разделитель"""
        result = string_utils.list_to_string(["Sky", "Pro"], "-")
        assert result == "Sky-Pro"

    def test_list_to_string_empty_list(self, string_utils):
        """Негативный тест: пустой список"""
        result = string_utils.list_to_string([])
        assert result == ""

    def test_list_to_string_single_item(self, string_utils):
        """Позитивный тест: один элемент"""
        result = string_utils.list_to_string(["hello"])
        assert result == "hello"

    def test_list_to_string_mixed_types(self, string_utils):
        """Позитивный тест: разные типы данных"""
        result = string_utils.list_to_string([1, "two", 3.0])
        assert result == "1, two, 3.0"
