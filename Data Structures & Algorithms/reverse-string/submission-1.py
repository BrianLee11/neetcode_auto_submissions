class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length_s = len(s)
        for index in range(length_s // 2):
            s[index], s[length_s - 1 - index] = s[length_s - 1 - index], s[index]
