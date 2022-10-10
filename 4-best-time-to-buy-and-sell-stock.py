#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from ast import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxP = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit)
            else:
                left = right
            right +=1
            
        return maxP
