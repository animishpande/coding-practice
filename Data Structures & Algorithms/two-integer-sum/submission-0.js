class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let a = nums[0];
        let b = nums[1];
        for(let i = 0; i < nums.length; i++) {
            for(let j = i + 1; j < nums.length; j++) {
                
                    a = nums[i];
                    b = nums[j];
                    if((a + b) == target) {
                        return [i, j]
                    }
                
            }
        }
    }
}
