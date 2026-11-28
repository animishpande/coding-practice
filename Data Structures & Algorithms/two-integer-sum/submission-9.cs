public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        List<int> res = new List<int>();
        for(int i = 0; i < nums.Length; i++)
        {
            for (int j = 1; j < nums.Length; j++) 
            {
                if (nums[i] + nums[j] == target && i != j)
                {
                    res.Add(i);
                    res.Add(j);
                    return res.ToArray();
                }
            }
        }
        return res.ToArray();
    }
}
