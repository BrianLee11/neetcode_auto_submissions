from typing import Dict, List # this adds type hints for List and Dict

# 1. get_dict_keys(age_dict: Dict[str, int]) -> List[str] 
# should take a dictionary of names and ages and 
# return a list of the names.
def get_dict_keys(age_dict: Dict[str, int]) -> List[str]:
    return list(age_dict.keys())

# 2. get_dict_values(age_dict: Dict[str, int]) -> List[int] 
# should take a dictionary of names and ages and 
# return a list of the ages.

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    return list(age_dict.values())

# do not modify below this line
dict_1 = {"John": 25, "Doe": 30, "Jane": 22}
dict_2 = {"NeetCode": 24, "NeetCode2": 25, "NeetCode3": 26}

print(get_dict_keys(dict_1))
print(get_dict_keys(dict_2))

print(get_dict_values(dict_1))
print(get_dict_values(dict_2))
