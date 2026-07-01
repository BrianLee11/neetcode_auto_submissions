from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        s_counter = Counter(s)

        number_odd = 0
        for value in s_counter.values():
            if value % 2 == 1:
                number_odd += 1
                if number_odd == 2:
                    return False
                
        return True
