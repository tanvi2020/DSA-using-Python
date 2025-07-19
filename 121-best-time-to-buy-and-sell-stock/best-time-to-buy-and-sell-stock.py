class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying_price=prices[0]
        max_profit=0
        for i in range(1,len(prices)):
            if prices[i]<buying_price:
                buying_price=prices[i]
            else:
                current_profit=prices[i]-buying_price
                max_profit=max(current_profit,max_profit)
        return max_profit


