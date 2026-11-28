public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var fl = new List<int>();
        for(int i = 0; i < nums.Length; i++)
        {
            for(int j = i + 1; j < nums.Length; j++)
            {
                var tar = nums[i] + nums[j];
                if(tar == target)
                {
                    fl.Add(i);
                    fl.Add(j);
                }
            }
        }
        return fl.ToArray();
    }
}
