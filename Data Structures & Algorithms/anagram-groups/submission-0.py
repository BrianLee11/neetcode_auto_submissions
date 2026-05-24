class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        myArray = []     

        for string in strs:
            if len(myArray) == 0:
                myArray.append([string])
                continue
            else:
                for index in range(len(myArray)):
                    if sorted(string) == sorted(myArray[index][0]):
                        myArray[index].append(string)
                        break
                    elif index == len(myArray) - 1:
                        myArray.append([string])

        return myArray