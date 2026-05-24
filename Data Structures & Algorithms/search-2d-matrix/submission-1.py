class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lengthN = len(matrix)
        lengthM = len(matrix[0])
                
        indexN = 0
        
        #print(f'lengthN: {lengthN}')
        
        if lengthN == 1:
            targetMatrix = matrix[0]
            #print(targetMatrix)
        
        else:
            while (indexN < lengthN - 1):
                
                if matrix[indexN][lengthM - 1] < target:
                    indexN += 1                
                else:
                    break
            
            #print(indexN)
            targetMatrix = matrix[indexN]
               
    
        # next
        if target not in targetMatrix:
            return False
        
        else:
            
            leftIndex = 0
            rightIndex = len(targetMatrix) - 1
            
            while (leftIndex <= rightIndex):
                midIndex = (leftIndex + rightIndex) // 2
                
                if targetMatrix[midIndex] == target:
                    indexM = midIndex
                    return True

                elif targetMatrix[midIndex] < target:
                    leftIndex = midIndex + 1
                
                else:
                    rightIndex = midIndex - 1