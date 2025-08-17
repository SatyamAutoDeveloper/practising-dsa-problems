class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        max_profit = 0
        for sell in range(1, n):
            profit = prices[sell] - prices[sell-1]
            if profit > 0:
                max_profit += profit
            buy = sell
        return max_profit
        
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4])) 

"""
The provided code calculates the maximum profit from multiple stock transactions by summing all positive differences between consecutive prices.

Time complexity:
- The algorithm iterates through the list of prices exactly once, from index 1 to n-1.
- Each iteration performs a constant amount of work (calculating the difference and an if check).
- Therefore, the overall time complexity is O(n), where n is the number of prices.

Space complexity:
- The algorithm uses a fixed amount of extra space: variables for n, max_profit, profit, and buy.
- No additional data structures proportional to input size are used.
- Hence, the space complexity is O(1).

In summary:
Time complexity: O(n)
Space complexity: O(1)
"""


"""
Solution 1:: TC: O(n), SC: O(1)

def maxProfit(self, prices):
	n = len(prices)
	buy = 0
	sell = 1
	max_profit = 0
	while sell < n:
		profit = prices[sell] - prices[buy]
		if profit > 0:
			max_profit += profit
		buy += 1
		sell += 1
	return max_profit
"""