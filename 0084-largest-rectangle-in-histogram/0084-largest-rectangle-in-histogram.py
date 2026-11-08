class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxa = 0
        stk = []
        for i,j in enumerate(heights):
            start = i
            while stk and stk[-1][1] > j:
                index,height = stk.pop()
                maxa = max(maxa,(height * (i-index)))
                start = index
            stk.append((start,j))
        
        for i,j in stk:
            maxa = max(maxa,(j*(len(heights)-i)))
        return maxa
