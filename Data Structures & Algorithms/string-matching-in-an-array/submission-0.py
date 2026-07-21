from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words_by_length = sorted(words, key=lambda word: len(word))
        common = []

        for left_index in range(len(words_by_length) - 1):
            left_word = words_by_length[left_index]

            for right_index in range(len(words_by_length) - 1, left_index, - 1):
                right_word = words_by_length[right_index]

                if left_word in right_word:
                    common.append(left_word)
                    break

        return common
