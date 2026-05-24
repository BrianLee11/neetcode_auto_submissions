class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> numberSet;

        for (int num : nums){
            if (numberSet.find(num) != numberSet.end()){
                return true;
            }
            else {
                numberSet.insert(num);
            }
        }

        return false;
    }
};