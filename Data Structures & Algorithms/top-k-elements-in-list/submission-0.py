class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # create hash map
        dictionary = {}

        for number in nums:
            if number in dictionary:
                dictionary[number] += 1
            else:
                dictionary[number] = 1

        # sort the hash map (dicitionary), in descending order
        sorted_frequency = dict(sorted(dictionary.items(), key = lambda item: -item[1]))
        sorted_value = list(sorted_frequency.keys())

        # generate k-frequency elements
        sorted_array = []

        for index in range(k):
            sorted_array.append(sorted_value[index])

        return sorted_array