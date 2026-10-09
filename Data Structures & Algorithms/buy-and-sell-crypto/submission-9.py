class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = 0
        b = 1
        maxProfit = 0
        while len(prices) > b:
            if prices[b] > prices[a]:
                profit = prices[b] - prices[a]
                maxProfit = max(profit, maxProfit)
            else:
                a = b
            b += 1
        return maxProfit