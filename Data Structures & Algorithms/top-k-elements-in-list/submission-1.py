class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] +=1
            else:
                d[i] = 1
        sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True)) 
        s = list(sorted_dict)
        a = []
        for i in range(k):
            a.append(s[i])
        return a

            
        
        