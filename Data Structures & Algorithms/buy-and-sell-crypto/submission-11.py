class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                max_p = max(profit, max_p)
            r += 1
        return max_p