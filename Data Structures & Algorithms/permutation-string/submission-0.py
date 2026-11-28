class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        l = 0
        r = n
        v = sorted(s1)
        for i in range(len(s2)):
            s3 = s2[l:r]
            if sorted(s3) == v:
                return True
            elif r == len(s2):
                return False
            else:
                l += 1
                r += 1
        
        return False
        