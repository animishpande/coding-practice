class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        print(nums3)
        l, r = 0, len(nums3) - 1
        res = 0
    
        m = (l + r) // 2
        print(m)
        if len(nums3) % 2 == 0:
            res = (nums3[m] + nums3[m+1]) / 2
            print(res)
        else:
            res = nums3[m]
        
        # print(res)
        return res

        

        
        