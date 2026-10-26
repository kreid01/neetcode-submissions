class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

         for i, x in enumerate(nums): 
            for  j, y in enumerate(nums):
                print(x, y,i,j)
                if x == y and i != j:
                    return True
                   
         return False

    
            