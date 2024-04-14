"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

## Solution

This problem requires the Sliding Window technique.

Given the constraint that a sale must occur after a purchase with the aim of maximizing profit, one can traverse through the list of prices while focusing on two primary considerations:

1. Is this price cheaper than any other price I've seen before?
2. If I subtract current price by the cheapest price I've found, does this yield a greater profit than what I've seen so far?

An interesting observation is that if the first condition is met, the second condition automatically becomes irrelevant for that iteration, eliminating the need for further verification at that point.

"""

def get_best_profit(prices_list, max_profit_if_negative=0):

    max_gain = 0
    cheapest_price = prices_list[0]
    
    if len(prices_list) < 2:
        return 0
    
    for price in prices_list:
        if price < cheapest_price:
            cheapest_price = price
            
        elif price - cheapest_price > max_gain:
            max_gain = price - cheapest_price
            
        else:
            continue
    return max(max_gain, max_profit_if_negative)

# test 1
prices_list = [7,1,5,3,6,4]

result = get_best_profit(prices_list)
expected_result = 5

assert result == expected_result

# test 2
prices_list = [7,6,4,3,1]

result = get_best_profit(prices_list)
expected_result = 0

assert result == expected_result


