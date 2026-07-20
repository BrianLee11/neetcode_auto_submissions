from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        int_index = 0
        target_string = strs[0]
        len_target_string = len(target_string)
        isFindLastIndex = False

        while not isFindLastIndex:
            if int_index >= len_target_string:
                break

            else:
                target_element = target_string[int_index]

                for string in strs[1:]:
                    if int_index >= len(string):
                        isFindLastIndex = True
                        break

                    else:
                        if target_element != string[int_index]:
                            isFindLastIndex = True
                            break

                if isFindLastIndex == False:
                    int_index += 1

        if int_index == 0:
            return ""

        else:
            return target_string[:int_index]