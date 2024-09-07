class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        minscore = float('inf')
        maxprofit = 0

        for i in range(n):
            if prices[i] < minscore:
                minscore = prices[i]
            elif prices[i] - minscore > maxprofit:
                maxprofit = prices[i] - minscore
        return maxprofit