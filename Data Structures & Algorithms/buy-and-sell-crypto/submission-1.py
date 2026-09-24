class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # m = 0
        # for i in range(len(prices)):
        #     for j in range(i,len(prices)):
        #         if prices[i]<prices[j]:
        #             m=max(m,prices[j] - prices[i])
        #         else:
        #             m = max(m,0)
        # return m 
        l,r = 0,1
        maxP = 0 

        while r <len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l=r
            r+=1
        return maxP
        
        
        

