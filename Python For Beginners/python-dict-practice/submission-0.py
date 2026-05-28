from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    my_dictionary = {}
    for character in word:
      if character in my_dictionary:
        my_dictionary[character] += 1
      else:
        my_dictionary[character] = 1

    return my_dictionary

# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
