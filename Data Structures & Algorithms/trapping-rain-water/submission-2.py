class Solution:
    def trap(self, height: List[int]) -> int:
        lwall, rwall = 0, 0
        n = len(height)
        maxL = [0]*n
        maxR = [0]*n

        for i in range(n):
            j = -i - 1
            maxL[i] = lwall
            maxR[j] = rwall
            lwall = max(lwall, height[i])
            rwall = max(rwall, height[j])

        summ = 0
        for i in range(n):
            pot = min(maxL[i], maxR[i])
            summ += max(0, pot - height[i])

        return summ