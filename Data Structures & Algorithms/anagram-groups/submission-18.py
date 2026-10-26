class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        top = []
        found = []
        
        for i, x in enumerate(strs):
            sub = [x]
            if x in found: 
                continue
            for j, y in enumerate(strs):
                if i != j and sorted(x) == sorted(y) and y not in found:
                    sub.append(y)
            top.append(sub)
            found.extend(sub)
        return top
