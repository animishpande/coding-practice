public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) {
            return false;
        }
        var charS = s.ToCharArray();
        var charT = t.ToCharArray();
        Array.Sort(charS);
        Array.Sort(charT);
        var newS = new string(charS);
        var newT = new string(charT);
        return newS.Equals(newT);
    }
}
