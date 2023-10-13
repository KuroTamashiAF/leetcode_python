"""
Given an integer x, return true if x is a
palindrome
, and false otherwise.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:  # 1
        numb = x
        if x < 0:
            return False
        if x is None:
            return False
        reverse_number = 0
        while numb > 0:
            remainder = numb % 10
            reverse_number = reverse_number * 10 + remainder  # 12
            numb //= 10
        if reverse_number == x:
            return True
        else:
            return False


if __name__ == '__main__':
    s1 = Solution()
    print(s1.isPalindrome(222))
