class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_p = 0
        for r in range(1, len(prices)):
            if prices[l] > prices[r] or prices[l] == prices[r]:
                l = r
            profit = prices[r] - prices[l]
            max_p = max(profit, max_p)
        return max_p