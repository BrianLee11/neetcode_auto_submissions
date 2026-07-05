class Solution:
    def climbStairs(self, n: int) -> int:
        dictionary_steps = {0: 1, 1: 1}

        for index in range(2, n + 1):
            dictionary_steps[index] = dictionary_steps[index - 1] + dictionary_steps[index - 2]

        return dictionary_steps[n]