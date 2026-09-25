class Solution:
    def trap(self, height: List[int]) -> int:
        # l = 0
        # w = 0
        # for i in range(len(height)):
        #     r=0
        #     l = max(height[i],l)
        #     for j in range(i+1,len(height)):
        #         r = max(height[j],r)
        #     if min(r,l) - height[i] > 0:
        #         w+=(min(r,l) - height[i])         
        # return w
        l2r = []
        r2l = []
        l,r = 0,0
        for i in range(len(height)):
            l = max(height[i],l)
            l2r.append(l)
        for i in range(len(height)-1,-1,-1):
            r = max(height[i],r)
            r2l.append(r)
        r2l = r2l[::-1]
        w = 0
        for i in range(len(height)):
            if min(l2r[i],r2l[i]) - height[i] >0:
                w+= min(l2r[i],r2l[i]) - height[i]
        return w
