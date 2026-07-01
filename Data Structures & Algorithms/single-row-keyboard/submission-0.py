class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        travelled_distance = keyboard.index(word[0])

        for index_char in range(len(word) - 1):
            travelled_distance += abs(keyboard.index(word[index_char]) - keyboard.index(word[index_char + 1]))

        return travelled_distance

    