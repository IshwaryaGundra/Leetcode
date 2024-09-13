class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float('-inf')
        print(max_profit)
        mini = prices[0]
        for i in range(1,len(prices)):
            if prices[i]<mini:
                mini=prices[i]
            max_profit = max(max_profit,prices[i]-mini)
        if max_profit<=0:
            return 0
        return max_profit