import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_letters_numbers = re.findall(r"[0-9a-zA-Z]", s.lower())
        s_joined = ''.join(s_letters_numbers)

        for index in range(len(s_joined) // 2):
            if s_joined[index] != s_joined[len(s_joined) - 1 - index]:
                return False

        return True