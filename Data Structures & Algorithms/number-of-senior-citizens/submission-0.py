from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        int_num_seniors = 0

        for personalInfo in details:
            str_age = personalInfo[-4:-2]
            int_age = int(str_age)

            if int_age > 60:
                int_num_seniors += 1

        return int_num_seniors
