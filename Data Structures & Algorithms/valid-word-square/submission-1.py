from typing import List

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for row_index in range(len(words)):
            row_word = words[row_index]
            column_index = row_index

            for row_iterator in range(len(row_word)):
                try:
                    if row_word[row_iterator] != words[row_iterator][column_index]:
                        return False
                except IndexError:
                    return False

        return True