class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        maxLeftArr = []
        maxLeft = 0
        for x in height:
            if x > maxLeft:
                maxLeft = x
            maxLeftArr.append(maxLeft)

        maxRightArr = []
        maxRight = 0
        for i in range(len(height)):
            if height[-1 -i] > maxRight:
                maxRight = height[-1 -i]
            maxRightArr.insert(0, maxRight)

        print(maxLeftArr, maxRightArr)    

        for i in range(len(height)):     
            total = min(maxRightArr[i], maxLeftArr[i]) - height[i]
            if total > 0:
                res += total
        return res
        
    