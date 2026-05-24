public class Solution {
    public bool IsAnagram(string s, string t)
    {
        if (s.Length != t.Length)
        {
            return false;
        }
        
        Dictionary<char, int> mapS = new Dictionary<char, int> ();
        Dictionary<char, int> mapT = new Dictionary<char, int>();
        
        foreach (char c in s)
        {
            if (mapS.ContainsKey(c))
            {
                mapS[c] += 1;
            }
            else
            {
                mapS[c] = 1;
            }
        }

        foreach (char c in t)
        {
            if (mapT.ContainsKey(c))
            {
                mapT[c] += 1;
            }
            else
            {
                mapT[c] = 1;
            }
        }
        
        
        // print the results
        foreach (KeyValuePair<char, int> pair in mapS)
        {
            if (mapT.ContainsKey(pair.Key))
            {
                if (pair.Value != mapT[pair.Key])
                {
                    return false;
                }
            }
            else
            {
                return false;
            }
        }
        
        return true;
    }
}
