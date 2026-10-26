class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for i in range(len(tokens)):
            print(nums)
            c = tokens[i]
            if c == "+" or c =="*" or c == "/" or c == "-":
                n2 = nums.pop()
                n1 = nums.pop()
                n3 = 0
                if tokens[i] == "+":
                    n3 = n1 + n2
                if tokens[i] == "*":
                    n3 = n1 * n2
                if tokens[i] == "-":
                    n3 = n1 - n2
                if tokens[i] == "/":
                    n3 = int(n1 / n2)
                nums.append(n3)
            else:
                nums.append(int(tokens[i]))

        return int(nums[0])



