class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price < min_price:
                min_price = price

            current_profit = price - min_price

            if current_profit > max_profit:
                max_profit = current_profit      
        return max_profit
    
sol = Solution()
print("Max Profit ::",sol.maxProfit([7,1,5,3,6,4])) 


"""
The time complexity of this solution is O(n), where n is the number of prices in the input list. This is because the algorithm iterates through the list exactly once, performing constant-time operations (comparisons and updates) during each iteration.

The space complexity is O(1), as the algorithm uses only a fixed amount of additional space regardless of the input size. It maintains a few variables (min_price, max_profit, current_profit) but does not allocate any extra space proportional to the input list.
"""
     
"""
Solution 1:: TC: O(n), SC: O(1)

def maxProfit(self, prices):
    max_profit = 0
    buy = 0
    sell = 1
    while sell < len(prices):
        print(buy, sell, prices[sell], prices[buy])
        profit = prices[sell] - prices[buy]
        if prices[buy] < prices[sell]:
            max_profit = max(profit, max_profit)
        else:
            buy = sell
        sell += 1
            
    return max_profit
"""