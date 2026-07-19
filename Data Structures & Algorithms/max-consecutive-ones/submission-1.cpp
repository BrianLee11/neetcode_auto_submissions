#include <iostream>
#include <vector>

class Solution {
public:
    int findMaxConsecutiveOnes(std::vector<int>& nums) {
        int current_occurrence_1 = 0;
        int max_occurrence_1 = 0;

        for (int number : nums)
        {
            if (number == 0) {current_occurrence_1 = 0;}
            else {current_occurrence_1 += 1;}

            if (max_occurrence_1 < current_occurrence_1) 
            {max_occurrence_1 = current_occurrence_1;}
        }

        return max_occurrence_1;
    }
};