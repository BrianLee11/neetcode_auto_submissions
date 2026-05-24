class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distance_array = []
        point_array = []
        dictionary = {}

        for point in points:
            distance = (point[0]**2) + (point[1]**2)
            distance_array.append(distance)
            point_array.append(point)
            
            if distance not in dictionary:
                dictionary[distance] = [point]
            else:
                dictionary[distance].append(point)

        copy_distance_array = distance_array
        copy_distance_array.sort()

        output = []
        for index in range(k):
            target_value = copy_distance_array[index]

            output.append(dictionary[target_value][0])
            dictionary[target_value].remove(dictionary[target_value][0])

        return output
            





