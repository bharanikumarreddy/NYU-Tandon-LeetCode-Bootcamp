class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    # Two Pointer Approach

        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price  # Update min_price if current price is lower
            elif price - min_price > max_profit:
                max_profit = price - min_price  # Update max_profit if current profit is higher
        return max_profit


    # Time Complexity: O(n), where n is the number of days. We only need to traverse the list once.
    # Space Complexity: O(1), as we're only using a fixed amount of extra space.
    
'''The code defines a class called Solution. In Python, classes are used to create objects that have certain properties and behaviors.

Inside the Solution class, there is a method called maxProfit. This method takes in a list of integers called prices as input and returns an integer as output.

The method uses the "Two Pointer Approach" to solve the problem. This approach involves using two pointers to keep track of the minimum price and the maximum profit.

The variable min_price is initialized with a very large value (float('inf')). This is done to ensure that any price in the prices list will be smaller than the initial value of min_price.

The variable max_profit is initialized with 0. This variable will store the maximum profit that can be obtained from buying and selling stocks.

The code then iterates through each price in the prices list using a for loop.

Inside the loop, it checks if the current price is smaller than the current min_price. If it is, the min_price is updated to the current price. This ensures that min_price always stores the smallest price encountered so far.

If the current price minus the min_price is greater than the current max_profit, it means that selling at the current price would yield a higher profit. In that case, the max_profit is updated to the current profit.

After iterating through all the prices, the method returns the max_profit.

To summarize, this code uses the Two Pointer Approach to find the maximum profit that can be obtained by buying and selling stocks. It keeps track of the minimum price encountered so far and calculates the profit by subtracting the minimum price from the current price. Finally, it returns the maximum profit.'''