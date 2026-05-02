class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        list_of_profit = []
        for buy in range(len(prices)):
            for sell in range(buy+1, len(prices)):
                if prices[buy] > prices[sell]:
                    continue
                else:
                    profit = prices[sell] - prices[buy]
                    list_of_profit.append(profit)
        
        if len(list_of_profit) == 0:
            return 0
        return max(list_of_profit)