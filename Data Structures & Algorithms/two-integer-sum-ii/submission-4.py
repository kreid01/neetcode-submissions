class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        total = -10
        l = 0
        r = len(numbers) - 1
        while total != target:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            elif total < target:
                l+=1
            else:
                r-=1
