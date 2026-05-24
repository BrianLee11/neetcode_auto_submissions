class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zero_coordinate = []
        for i_index in range(len(matrix)):
            for j_index in range(len(matrix[0])):
                if matrix[i_index][j_index] == 0:
                    coordinate = [i_index, j_index]
                    zero_coordinate.append(coordinate)

        for coordinate in zero_coordinate:
            row_index = coordinate[0]
            column_index = coordinate[1]
            
            for index in range(len(matrix[row_index])):
                matrix[row_index][index] = 0
                
            for index in range(len(matrix)):
                matrix[index][column_index] = 0

        return    
        