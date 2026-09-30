class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        f = {}
        l,best=0,0
        max_count = 0
        for r in range(len(s)):
            if s[r] not in f:
                f[s[r]] = 1
                max_count = max(f[s[r]], max_count)

            else:
                f[s[r]]+=1
                max_count = max(f[s[r]], max_count)
            while ((r-l+1) - max_count) > k:
                    f[s[l]]-=1
                    l+=1
            best = max(best,r-l+1)
        return best
            
        

        # f = {}
        # for i in s:
        #     if i not in f:
        #         f[i] = 1
        #     else:  
        #         f[i]+=1
        # f = dict(sorted(f.items(),key=lambda x:x[1],reverse=True))
        # char = ""
        # max_v = 0
        # for i in f:
        #     if f[i] >= max_v:
        #         max_v = f[i]
        #         char=i
        #         break
        # l = 0
        # update = 0
        # f_s =""
        # for r in range(len(s)):    
        #     if s[l]!=s[r] and update < k:
        #         f_s+=char
        #         update+=1     
        #     else:
        #         f_s+=s[r]
        # m = 0
        # lrg = 0
        # for r in range(len(f_s)):
        #     if f_s[l] == f_s[r]:
        #         lrg+=1
        #         m = max(m,lrg)
        #     else:
        #         lrg = 1
        #         l+=1
        # return m

# X = Solution()
# X.characterReplacement("AAABABB",1)
                      