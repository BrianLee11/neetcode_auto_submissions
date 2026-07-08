class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for index in range(len(s) // 2):
            s[index], s[len(s) - 1 - index] = s[len(s) - 1 - index], s[index]


        