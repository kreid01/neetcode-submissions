class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        print(s , nums)
        if len(s) != len(nums):
            return True
        else:         
            return False

    
            