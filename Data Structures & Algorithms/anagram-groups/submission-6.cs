public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> res = new Dictionary<string, List<string>>();
        
        foreach(string s in strs) {
            char[] sArr = s.ToCharArray();
            Array.Sort(sArr);
            string sVal = new string(sArr);
            if (!res.ContainsKey(sVal)) {
                res[sVal] = new List<string>();
            }
            res[sVal].Add(s);
        }

        return res.Values.ToList();
    }
}
