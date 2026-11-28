public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var res = new Dictionary<string, List<string>>();
        foreach(string s in strs)
        {
            var sa = s.ToCharArray();
            Array.Sort(sa);
            var sn = new string(sa);
            if(!res.ContainsKey(sn))
            {
                res[sn] = new List<string>();
            }
            res[sn].Add(s);
        }
        return res.Values.ToList();
    }
}
