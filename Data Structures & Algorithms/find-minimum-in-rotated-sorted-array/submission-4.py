class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 1, len(nums) - 1
        minv = nums[0]

        while l <= r:
            v = min(nums[l], nums[r])
            minv = min(minv, v)
            if nums[l] > nums[r]:
                l += 1
            else:
                r -= 1

        return minv
        