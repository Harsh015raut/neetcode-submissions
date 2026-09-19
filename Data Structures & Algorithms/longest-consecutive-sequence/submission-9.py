from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # seq = list(set((sorted(nums))))
        # lst = []
        # for i in range(len(seq)):
        #     if i==0:
        #         lst.append(seq[i])
        #     elif seq[i]==seq[i-1] + 1:
        #         lst.append(seq[i])
        #     elif seq[i]!=seq[i-1] + 1:
        #         lst = []
        #         lst.append(seq[i])
        # return len(lst)
        seq = list(sorted(set(nums)))
        lst = defaultdict(int)
        runs = 0 
        for i in range(len(seq)):
            if i==0:
                lst[runs]+=1
            elif seq[i]==seq[i-1]+1:
                lst[runs]+=1
            else:
                runs+=1
                lst[runs]+=1
        return max(lst.values(),default=0)
