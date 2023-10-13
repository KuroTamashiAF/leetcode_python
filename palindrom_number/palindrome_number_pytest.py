import pytest
from palindrome_number import Solution


@pytest.fixture
def data():
    s1 = Solution()
    return s1


def test_palindrome_number_is_true(data):
    assert data.isPalindrome(121) is True
    assert data.isPalindrome(222) is True
    assert data.isPalindrome(12321) is True


def test_palindrome_number_is_false(data):
    assert data.isPalindrome(123) is False
    assert data.isPalindrome(-321) is False
    assert data.isPalindrome(456125) is False


if __name__ == '__main__':
    pytest.main(['-v'])
