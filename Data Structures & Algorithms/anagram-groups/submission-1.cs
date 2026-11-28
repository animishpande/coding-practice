public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var res = new Dictionary<string, List<string>>();
        foreach(string s in strs)
        {
            char[] v = s.ToCharArray();
            Array.Sort(v);
            string val = new string(v);
            if(!res.ContainsKey(val))
            {
                res[val] = new List<string>();
            }
            res[val].Add(s);
        }
        return res.Values.ToList();
    }
}
