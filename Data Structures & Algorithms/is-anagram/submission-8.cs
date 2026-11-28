public class Solution {
    public bool IsAnagram(string s, string t) {
        var sArr = s.ToCharArray();
        var tArr = t.ToCharArray();
        Array.Sort(sArr);
        Array.Sort(tArr);
        string sN = new string(sArr);
        string tN = new string(tArr);
        return sN == tN;
    }
}
