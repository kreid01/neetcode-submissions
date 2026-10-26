class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        count = 1
        maxC = 1
        sort = sorted(nums)
        print(sort)
        for i in range(1, len(sort)):
            print(sort[i], count)
            if sort[i] == sort[i - 1] + 1:
                count += 1
                if maxC <= count:
                    maxC = count
            elif sort[i] == sort[i - 1]:
                continue;
            else:
                count = 1
        return maxC