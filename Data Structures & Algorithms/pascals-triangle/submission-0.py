from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        elif numRows == 3:
            return [[1], [1,1], [1,2,1]]
        else:
            dictionary_triangle = {1: [1], 2: [1,1], 3:[1,2,1]}
            combined_triangles = [[1], [1, 1], [1, 2, 1]]

            for index in range(4, numRows + 1, 1):
                target_triangle = dictionary_triangle[index - 1]
                receive_array = [1]
                for index_element in range(len(target_triangle) - 1):
                    receive_array.append(target_triangle[index_element] + target_triangle[index_element + 1])
                receive_array.append(1)

                dictionary_triangle[index] = receive_array
                combined_triangles.append(receive_array)

            return combined_triangles