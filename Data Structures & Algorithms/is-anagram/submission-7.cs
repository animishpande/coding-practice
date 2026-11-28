// using System.Collections.Generic;

public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) 
        {
            return false;
        }

        var sa = s.ToCharArray();
        var ta = t.ToCharArray();
        Dictionary<char, int> sD = new Dictionary<char, int>();
        Dictionary<char, int> tD = new Dictionary<char, int>();
        
        for(int i = 0; i < sa.Length; i++)
        {
            if (sD.ContainsKey(sa[i])) 
            {
                int val = sD[sa[i]];
                sD[sa[i]] =  val + 1;
            }
            else
            {
                sD[sa[i]] = 1;
            }
            if (tD.ContainsKey(ta[i])) 
            {
                int val = tD[ta[i]];
                tD[ta[i]] =  val + 1;
            }
            else
            {
                tD[ta[i]] = 1;
            }
            
        }
        foreach(var kvp in sD)
        {
            Console.WriteLine($"Key: {kvp.Key}, Value: {kvp.Value}");
        }
        foreach(var kvp in tD)
        {
            Console.WriteLine($"Key: {kvp.Key}, Value: {kvp.Value}");
        }
        return tD.Count == sD.Count && !tD.Except(sD).Any();
    }
}
