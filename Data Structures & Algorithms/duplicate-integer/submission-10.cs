public class Solution {
    public bool hasDuplicate(int[] nums) {
        var vals = new List<int> {};
        foreach(int i in nums) {
            if (vals.Contains(i)) {
                return true;
            };
            vals.Add(i);
        };
        return false;
    }
}