class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = profit = -1
        for x in prices:
            if buyPrice == -1:
                buyPrice = x
            elif x < buyPrice:
                buyPrice = x
            else: 
                if profit == -1 or profit < x - buyPrice :
                    profit = x - buyPrice
        if profit == -1:
            profit = 0
        
        return profit
                
            
                
        