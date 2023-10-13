import pytest
from roman_to_integer import Solution


@pytest.fixture
def data():
    s1 = Solution()
    return s1


def test_roman_to_integer_numbers(data):
    assert data.romanToInt("III") == 3
    assert data.romanToInt("IV") == 4
    assert data.romanToInt("IV") == 4
    assert data.romanToInt("LVIII") == 58
    assert data.romanToInt("MCMXCIV") == 1994


if __name__ == '__main__':
    pytest.main(['-v'])
