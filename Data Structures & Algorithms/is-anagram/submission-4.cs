public class Solution {
    public bool IsAnagram(string s, string t) {
        char[] sa = s.ToCharArray();
        char[] ta = t.ToCharArray();
        Array.Sort(sa);
        Array.Sort(ta);
        string sn = new string(sa);
        string tn = new string(ta);
        if(sn.Equals(tn))
        {
            return true;
        }
        return false;
    }
}
