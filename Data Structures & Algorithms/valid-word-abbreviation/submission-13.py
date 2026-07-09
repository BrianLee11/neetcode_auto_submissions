import re

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        int_length_word = len(word)
        str_list_split_chars = re.findall(r'[a-z]|[0-9]+', abbr)
        str_joined_abbr = ""
        void_character = '_'

        for element in str_list_split_chars:
            if element[0] == "0":
                return False
            
            try:
                number = int(element)
                str_joined_abbr += void_character * number
            except:
                str_joined_abbr += element

        if int_length_word != len(str_joined_abbr):
            return False

        else:
            for index in range(int_length_word):
                if str_joined_abbr[index] != "_" and word[index] != str_joined_abbr[index]:
                    return False

        return True
