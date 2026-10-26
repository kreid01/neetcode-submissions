class Solution:
    def isValid(self, s: str) -> bool:
        par = { ")" : "(", "]" : "[", "}" : "{" } 
        stack = []
        for x in s:
            if len(stack) > 0 and x in par.keys() and stack[-1] == par[x]:
                stack.pop()
            else:
                stack.append(x)
        print(stack)
        return len(stack) == 0