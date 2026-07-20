#include <iostream>
#include <vector>
#include <string>

class Solution 
{
    public:
    std::string longestCommonPrefix(std::vector <std::string> strs)
    {
        int int_index = 0;
        std::string target_string = strs[0];
        int int_size_target_string = target_string.size();
        bool bool_isFindLastIndex = false;

        while (! bool_isFindLastIndex)
        {
            if (int_index >= int_size_target_string) {break;}
            else
                {
                    char target_element = target_string[int_index];

                    for (std::size_t index = 1; index < strs.size(); ++index)
                        {                            
                            std::string candidate_string = strs[index];

                            if (int_index >= candidate_string.size())
                            {
                                bool_isFindLastIndex = true;
                                break;
                            }
                            else 
                            {
                                if (target_element != candidate_string[int_index])
                                {
                                    bool_isFindLastIndex = true;
                                    break;
                                }
                            }
                        }
                    
                    if (bool_isFindLastIndex == false) {int_index += 1;}; 
                }
        } // end of while

        if (int_index == 0) {return "";}
        else {return target_string.substr(0,int_index);};
    }
};