#include <vector>
#include <string>
#include <iostream>

class Solution {
public:
    int countSeniors(std::vector<std::string>& details) {        
        int index_begin = 11;
        std::string str_age = "";
        int int_age = 0;
        int count_age_over_60 = 0;


        for (std::string personalInfo : details)
            {
                str_age = personalInfo.substr(index_begin, 2);
                int_age = stoi(str_age);
                if (int_age > 60){count_age_over_60 += 1;};
            }
            
    return count_age_over_60;
    }
};