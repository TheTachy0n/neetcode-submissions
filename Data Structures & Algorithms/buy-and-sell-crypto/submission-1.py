class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Goal is to maximix=ze the profit from the trade,(buy at the lowest and sell at the highest prize)
        '''
        1. Brute Force 
        - we would use a nested for loops to compare every value to every other value
        - in the 1st loop assume every price as the buy price initially
        - in the 2nd loop find a sell price and change the res value accordingly
        '''
        '''
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1, len(prices)):
                sell = prices[j]
                res = max(res, (sell - buy))
        return res
        '''
        '''
        2. Sliding window
        - set the min price as the 1st element of the array prices
        - set the max profit to 0
        - in a for loop if the given price is less than the min price -> update the min_price
        - else the current profit is the price - min_price
        - now for the max_profit we can say its the max of curr_profit and max_profit itself
        - return the max profit
        '''
        min_price = prices[0]
        max_profit = 0
        for i in prices:
            if i < min_price:
                min_price = i
            else:
                curr_profit = i - min_price
                max_profit = max(max_profit, curr_profit)
        return max_profit