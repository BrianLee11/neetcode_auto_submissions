class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        string_array = []
        for digit in digits:
            string_array.append(str(digit))
        
        string_array = ''.join(string_array)
        int_string = int(string_array) + 1

        string_array = str(int_string)

        output = []

        for index in range(len(string_array)):
            output.append(int(string_array[index]))




        

        return output

  


        




