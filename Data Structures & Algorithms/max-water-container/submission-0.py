class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        l = 0
        r = len(heights) - 1
        for _ in range(len(heights)):
            print(r - l, min(heights[r], heights[l]))
            total = (r - l)  * min(heights[r], heights[l])
            if total > result: 
                result = total
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return result