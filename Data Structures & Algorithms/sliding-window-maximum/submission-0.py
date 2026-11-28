class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k
        ml = []

        for i in range(len(nums)):
            v = nums[l:r]
            ml.append(max(v))
            if r == len(nums):
                break
            else:
                l += 1
                r += 1
        
        return ml

        