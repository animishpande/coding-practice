from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myList = set(nums)
        print(myList)
        if len(myList) < len(nums):
            return True
        else:
            return False

         