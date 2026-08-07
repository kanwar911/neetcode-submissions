class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        maxP, profit = 0, 0
        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
            elif prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
            if profit > maxP:
                maxP = profit
            sell += 1
        return maxP