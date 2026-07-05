# based on last try 01

from typing import List
import re

class Letter:
    # example: 'N10' indicates char = N, occurrence = 10
    def __init__(self, letter_info: List[str]):
        self.char = letter_info[0]
        self.occurrence = int(letter_info[1:])

class StringIterator:
    def __init__(self, compressedString: str):
        # example of a given string: "N1e2t1C1o1d1e1"
        # using regular expression, creates a list of {char}{ocurrence}
        # example: ['N10', 'e2', 't1', 'C1', 'o1', 'd1', 'e11']
        list_letter_info = re.findall(r"[A-Za-z][0-9]+", compressedString)

        # list of instances of the class Letter
        self.list_letter = []

        # (continue) iterate each letter_info to instances of the class Letter
        for letter_info in list_letter_info:
            letter = Letter(letter_info)
            self.list_letter.append(letter)

        # helps to determine the length of list_letter
        # not necessary, but helps lessen the number of calculations
        self.len_list_letter = len(self.list_letter)

        # for location purpose, etc
        self.current_index_list_letter = -1
        self.current_letter = ''
        self.current_remaining_occurrence = 0

    # method next
    def next(self) -> str:
        # if remaining occurrence is positive, reduce occurrence by 1
        # return the current letter
        if self.current_remaining_occurrence > 0:
            self.current_remaining_occurrence -= 1
            return self.current_letter

        else:
            # if remaining occurrence is zero
            # it's either
            # 1) we reached the end of the list,
            # 2) not reached the end of the list, we should move to the next letter

            # 1) test: have we reached the end of the list?
            if self.current_index_list_letter == self.len_list_letter:
                return " "

            # test: have we not reached the end of the list?
            # 2) not reached the end of the list
            else:
                # move to the next letter
                self.current_index_list_letter += 1

                # set the letter
                self.current_letter = self.list_letter[self.current_index_list_letter].char

                # set the occurrence
                self.current_remaining_occurrence = self.list_letter[self.current_index_list_letter].occurrence - 1
                # print(self.current_letter)
                return self.current_letter

    # method hasNext
    def hasNext(self) -> bool:
        if self.current_remaining_occurrence > 0:
            return True
        else:
            if self.current_index_list_letter < self.len_list_letter:
                return True
            else:
                return False



