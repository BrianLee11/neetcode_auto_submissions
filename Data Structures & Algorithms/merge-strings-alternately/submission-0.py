class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)

        full_length = len1 + len2
        list_str_chars = []
        min_length = min(len1, len2)

        index_word1: int = 0
        index_word2: int = 0

        while index_word1 < len1 and index_word2 < len2:
            list_str_chars.append(word1[index_word1])
            list_str_chars.append(word2[index_word2])

            index_word1 += 1
            index_word2 += 1

        for index in range(index_word1, len1, 1):
            list_str_chars.append(word1[index])

        for index in range(index_word2, len2, 1):
            list_str_chars.append(word2[index])

        joined_word = ''.join(list_str_chars)
        return joined_word