class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        for x in s:
            if x in t:
                t = t.replace(x, "", 1)
            
        if len(t) == 0: 
            return True
        else: 
            return False
