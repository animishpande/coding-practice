public class Solution {
        public void checkDup(int i, int[] nums, HashSet<int> set) 
        {
            Console.WriteLine("i : " + i);
            if (i < nums.Length) 
            {
                set.Add(nums[i]);
                i += 1;
                checkDup(i, nums, set);
            }
        }
    public bool hasDuplicate(int[] nums) {
        HashSet<int> set = new HashSet<int>();
        checkDup(0, nums, set);
        Console.WriteLine(set.Count);
        Console.WriteLine(nums.Length);
        if (set.Count == nums.Length) 
        {
            return false;
        }
        return true;
    }
}