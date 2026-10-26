class Solution:
    def isPalindrome(self, s: str) -> bool:
        nw = ""
        for x in s:
            if x.isalnum():
                nw += x.lower()
        return nw == nw[::-1]
        
