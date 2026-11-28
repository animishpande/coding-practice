class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = set()
        for i in range(len(nums)):
            if nums[i] in l:
                return nums[i]
            else:
                l.add(nums[i])

        return 0

        