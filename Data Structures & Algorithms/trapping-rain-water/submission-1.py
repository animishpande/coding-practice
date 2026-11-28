class Solution:
    def trap(self, height: List[int]) -> int:
        l_wall, r_wall = 0, 0
        n = len(height)
        maxL = [0] * n
        maxR = [0] * n

        for i in range(n):
            j = -i - 1
            maxL[i] = l_wall
            maxR[j] = r_wall
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])
            
        summ = 0    
        for i in range(n):
            pot = min(maxL[i], maxR[i])
            summ += max(0, pot - height[i])

        return summ