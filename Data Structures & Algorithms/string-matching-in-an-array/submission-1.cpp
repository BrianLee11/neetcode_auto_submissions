#include <iostream>
#include <vector>
#include <string>
#include <algorithm> // for std::sort()

class Solution
{
    public:
    static bool compareByLength
(
    const std::string& a,
    const std::string& b
)
    {
        return a.size() < b.size();
    }

    std::vector <std::string> stringMatching(std::vector <std::string> words)
    {


        std::vector <std::string> words_by_length = words;

        std::sort(
            words_by_length.begin(),
            words_by_length.end(),
            compareByLength
        );

        std::vector <std::string> common = {};
        std::string left_word = "";
        std::string right_word = "";

        for (int left_index = 0; left_index < words_by_length.size(); ++left_index)
        {
            left_word = words_by_length[left_index];

            for (int right_index = words_by_length.size() - 1; left_index < right_index; --right_index)
            {
                right_word = words_by_length[right_index];

                if (right_word.find(left_word) != std::string::npos){
                    common.push_back(left_word);
                    break;
                }
            }
        }
        
        return common;
    }
};

