class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures
        n = len(temps)
        res = [0] * n
        stk = []

        # enumerate means i = index and t = value for each index
        for i, t in enumerate(temps):
            # we check if we have a value in the stack
            # if yes we then check if it is smaller than the next value
            # here stk[-1] is the top element of the stack and [0] is the value
            # since we are going to be storing tuples in stk like (value, index)
            while stk and stk[-1][0] < t:
                # if this condition is true, we pop the value from the stack
                # and add the difference of days into the res array
                stk_t, stk_i = stk.pop()
                res[stk_i] = i - stk_i

            # if the above condition is false, we append the value to stk
            stk.append((t, i))

        return res 

        
        
        