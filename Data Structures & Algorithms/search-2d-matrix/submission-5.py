class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0]) -1
        bot, top = 0, len(matrix) - 1
        ro = -1

        print(top, bot)
        
        while bot <= top:
            row = (top + bot) // 2
            if target < matrix[row][0]:
                top = row - 1
            elif target > matrix[row][-1]:
                bot = row  + 1
            else: 
                ro = row
                break
        print(r)

        while l <= r:
            m = (l + r) // 2
            print(matrix[ro][m], l ,r)
            if target == matrix[ro][m]:
                return True
            elif target < matrix[ro][m]:
                r = m - 1
            else:
                l = m + 1
        return False
