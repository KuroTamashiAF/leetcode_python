import pytest
from two_sum import Solution


@pytest.fixture()
def data():
    s_obj = Solution()
    return s_obj


def test_two_sum(data):
    assert data.twoSum([2, 7, 11, 15], 9)
    assert data.twoSum([3, 2, 4], 6)
    assert data.twoSum([3, 3], 6)


if __name__ == '__main__':
    pytest.main(['-v'])
