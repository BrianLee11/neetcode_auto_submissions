class Solution:
    def scoreOfString(self, s: str) -> int:
        sum_scores = 0
        for index in range(len(s) - 1):
            sum_scores += abs(ord(s[index]) - ord(s[index + 1]))

        return sum_scores