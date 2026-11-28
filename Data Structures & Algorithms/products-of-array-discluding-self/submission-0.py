class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return
        n = len(nums)
        mul = 1
        ans = []
        for i in range(n):
            for j in range(n):
                if i != j:
                    mul *= nums[j]
            ans.append(mul)
            mul = 1


        print(mul)
        print(ans)
        return ans
        