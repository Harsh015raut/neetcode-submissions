class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # p = 1
        # r=[]
        # l=[]
        # for i in range(len(nums)-1, -1, -1):
        #     r.append(p)
        #     p*=nums[i]
        # r = r[::-1]
        # p = 1
        # for j in range(len(nums)):
        #     if j == 0:
        #         l.append(p)
        #     else:
        #         p*=nums[j-1]
        #         l.append(p)
        # pr = []
        # for i in range(len(nums)):
        #     pr.append(r[i]*l[i])
        # return pr
        

        p = 1
        r = []
        l=[]
        for i in range(len(nums)-1,-1,-1):
            r.append(p)
            p*=nums[i]
        r=r[::-1]
        p=1
        for j in range(len(nums)):
            if j==0:
                p=1
                l.append(p) 
            else:
                p*=nums[j-1]
                l.append(p)
        pr = []
        for i in range(len(nums)):
            pr.append(r[i]*l[i])
        return pr










