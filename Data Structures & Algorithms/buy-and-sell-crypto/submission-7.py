class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = 0
        b = 1
        maxP = 0
        while b < len(prices):
            if prices[a] < prices[b]:
                profit = prices[b] - prices[a]
                maxP = max(maxP, profit)
            else:
                a = b
            b += 1
        return maxP
            