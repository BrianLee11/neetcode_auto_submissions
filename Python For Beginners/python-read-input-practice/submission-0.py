def add_two_numbers() -> int:
    user_input = input()
    list_string = user_input.split(',')
    return int(list_string[0]) + int(list_string[1])

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
