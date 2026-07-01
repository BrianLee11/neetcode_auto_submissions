from typing import List

class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        # test 1: they have the same length (i.e. the same number of words)
        if len(sentence1) != len(sentence2):
            return False
        else:
            # test 2: "similar"
            for index in range(len(sentence1)):
                word1 = sentence1[index]
                word2 = sentence2[index]

                # same word
                if word1 == word2:
                    continue

                else:
                    isSimilar = False
                    for pair in similarPairs:
                        if word1 in pair and word2 in pair:
                            isSimilar = True
                            break

                    if not isSimilar:
                        return False
        return True