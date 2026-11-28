public class Solution {
    public bool IsAnagram(string s, string t) {
        var sa = s.ToCharArray();
        var ta = t.ToCharArray();
        Array.Sort(sa);
        Array.Sort(ta);
        var sn = new string(sa);
        var tn = new string(ta);
        if(sn.Equals(tn))
        {
            return true;
        }
        return false;
    }
}
