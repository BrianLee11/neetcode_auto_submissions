class Solution:
    def check_palindrome(self, str_string) -> bool:
        length_string = len(str_string)
        for index in range(length_string // 2):
            if str_string[index] != str_string[length_string - 1 - index]:
                return False
        return True

    def validPalindrome(self, str_string: str) -> bool:
        length_strength = len(str_string)

        left = 0
        right = length_strength

        while left < right:
            if str_string[left] != str_string[right - 1]:
                return (self.check_palindrome(str_string[left + 1: right])
                        or self.check_palindrome((str_string[left : right - 1])))
            else:
                left += 1
                right -= 1

        return True



