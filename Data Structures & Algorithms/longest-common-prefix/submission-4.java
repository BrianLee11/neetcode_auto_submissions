public class Solution {    
    String longestCommonPrefix(String[] strs){
        int int_index =0;
        String target_string = strs[0];
        int int_size_target_string = target_string.length();
        Boolean bool_isFindLastIndex = false;

        while (! bool_isFindLastIndex)
        {
            if (int_index >= int_size_target_string) { break;}
            else 
            {
                char target_element = target_string.charAt(int_index);

                for (int index = 1; index < strs.length; ++index)
                {
                    String candidate_string = strs[index];

                    if (int_index >= candidate_string.length())
                    {
                        bool_isFindLastIndex = true;
                        break;
                    }
                    else
                    {
                        if (target_element != candidate_string.charAt(int_index))
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
        else {return target_string.substring(0, int_index);}        
    }
}