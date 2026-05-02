class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_res = 0
        while l<r and r<len(prices):
            res = prices[r] - prices[l]
            if res <= 0:
                l = r
            r += 1
            max_res = max(res, max_res)
        return max_res