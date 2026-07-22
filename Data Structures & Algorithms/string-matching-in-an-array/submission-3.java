public class Solution
    {
        static int compareByLength(String a, String b)
        {
            return Integer.compare(a.length(), b.length());      
        }

        public List<String> stringMatching(String[] words)
        {
            String[] wordsByLength = words.clone();
            
            Arrays.sort(wordsByLength, 
                        Solution::compareByLength);

            List<String> common = new ArrayList<>();
            String leftWord = "";
            String rightWord = "";

            for (int leftIndex = 0; 
                 leftIndex < wordsByLength.length; 
                 ++leftIndex)
                {
                    leftWord = wordsByLength[leftIndex];

                    for (int rightIndex = wordsByLength.length - 1; 
                         leftIndex < rightIndex; 
                         --rightIndex)
                        {
                            rightWord = wordsByLength[rightIndex];

                            if (rightWord.contains(leftWord)){
                                common.add(leftWord);
                                break;
                            }
                        }                    
                }
            return common;
        }
    }
