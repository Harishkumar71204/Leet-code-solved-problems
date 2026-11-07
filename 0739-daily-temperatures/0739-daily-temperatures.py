class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0]*len(temperatures)
        stk = []
        for i,cur in enumerate(temperatures):
            while stk and temperatures[stk[-1]] < cur:
                top = stk.pop()
                res[top] = i - top
            stk.append(i)
        return res