import pytest
from longest_common_prefix import Solution


@pytest.fixture()
def data():
    s1 = Solution()
    return s1


def test_longest_common_prefix_1(data):
    assert data.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"


def test_longest_common_prefix_2(data):
    assert data.longestCommonPrefix(["dog", "racecar", "car"]) == ""


def test_longest_common_prefix_3(data):
    assert data.longestCommonPrefix([""]) == ""


def test_longest_common_prefix_4(data):
    assert data.longestCommonPrefix(["cir", "car"]) == "c"


def test_longest_common_prefix_5(data):
    assert data.longestCommonPrefix(["reflower", "flow", "flight"]) == ""


def test_longest_common_prefix_6(data):
    assert data.longestCommonPrefix(["flower", "fkow"]) == "f"


def test_longest_common_prefix_7(data):
    assert data.longestCommonPrefix(["", ""]) == ""


if __name__ == '__main__':
    pytest.main(['-v'])
