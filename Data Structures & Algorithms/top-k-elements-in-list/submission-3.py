class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        r = defaultdict(int)
        for x in nums:
            r[x] += 1;

        final = []  
        print(r) 
        
        for key, value in sorted(r.items(), key=lambda item: item[1], reverse = True):
            final.append(key)

        return final[:k]
        



        