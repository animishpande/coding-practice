public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        var final = new List<int>();

        for(int i = 0; i < numbers.Length; i++)
        {
            for(int j = i + 1; j < numbers.Length; j++)
            {
                var addVal = numbers[i] + numbers[j];
                if(addVal == target)
                {
                    final.Add(i + 1);
                    final.Add(j + 1);
                    break;
                }
            }
        }
        return final.ToArray();
    }
}
