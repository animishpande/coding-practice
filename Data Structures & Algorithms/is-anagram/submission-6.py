class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sArr = list(s)
        tArr = list(t)
        sArr.sort()
        tArr.sort()
        a = "".join(sArr)
        b = "".join(tArr)
        return a == b
        