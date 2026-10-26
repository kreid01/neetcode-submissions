class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = []
        total = 1
        for i, x in enumerate(nums):
            if x == 0:
                zeros.append(i)
            else:
                total *= x
        
        if len(zeros) > 1:
            return [0] * len(nums)
        
        res = []
        for i, x in enumerate(nums):
            if i in zeros: 
                res.append(int(total))
            elif len(zeros) > 0 :
                res.append(0)
            else:
                res.append(int(total / x))
        
        return res