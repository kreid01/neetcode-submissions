class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums) 
        result = []

        for i, x in enumerate(sort):
            if i > 0 and x == sort[i - 1]:
                continue

            l, r = i + 1, len(sort) - 1
            while l < r:
                threeSum = x + sort[l] + sort[r]
                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
                else:
                    result.append([x, sort[l], sort[r]])
                    l += 1
                    while sort[l] == sort[l - 1] and l < r:
                        l += 1
               
        return result