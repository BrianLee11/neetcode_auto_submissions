class Solution(object):
    def isPalindrome(self, string):
        """
        :input type string1: str
        :output type: bool
        """        
        import re

        # Consider lowercase only
        lowercase_string = string.lower()

        # Remove non-alphanumeric characters,
        cleaned_string = re.sub(r'[^a-z0-9]', '', lowercase_string)

        for index in range(len(cleaned_string) // 2):
            if cleaned_string[index] != cleaned_string[len(cleaned_string) - index - 1]:
                return False

        return True