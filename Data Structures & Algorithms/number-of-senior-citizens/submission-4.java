class Solution {
    public int countSeniors(String[] details) {
                String str_age = "";
        int int_age = 0;
        int count_over_60 = 0;
        
        for (String detail : details){
            str_age = detail.substring(11,13);
            int_age = Integer.parseInt(str_age);

            if (int_age > 60) count_over_60 += 1;            
        }

        return count_over_60;
    }
}