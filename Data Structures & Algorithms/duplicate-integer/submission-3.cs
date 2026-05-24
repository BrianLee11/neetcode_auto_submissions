public class Solution {
    public bool hasDuplicate(int[] nums)
    {
        HashSet<int> numHash = new HashSet<int>();

        foreach (int num in nums)
        {
            if (numHash.Contains(num))
            {
                return true;
            }
            else
            {
                numHash.Add(num);
            }
        }
        return false;
    }
}