class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = {}
        for i in range(len(nums)):
            print(l.get(nums[i]))
            if l.get(nums[i]) is not None:
                return True
            l[nums[i]] = i
        
        print(l)
        return False
            
        