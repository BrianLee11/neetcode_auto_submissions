from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        queue = deque()

        for element in s:
            if not queue:
                queue.append(element)

            elif element in {"(", "{", "["}:
                queue.append(element)

            else:
                str_last_element = queue[-1]

                if element == ")":
                    if not str_last_element == "(":
                        return False

                elif element == "}":
                    if not str_last_element == "{":
                        return False

                elif element == "]":
                    if not str_last_element == "[":
                        return False

                queue.pop()

        if queue:
            return False
        else:
            return True
