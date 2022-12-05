# Time complexity: O(n)
# Space complexity: O(1)
from typing import List

class TestSolution:
  def maxProfit(self):
    solution = Solution()
    assert solution.maxProfit([7,1,5,3,6,4]) == 5
    assert solution.maxProfit([7,6,4,3,1]) == 0
    assert solution.maxProfit([1,2]) == 1
    assert solution.maxProfit([2,1,2,1,0,1,2]) == 2
    assert solution.maxProfit([1,2,4]) == 3

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    min_price = prices[0]
    max_profit = 0
    for price in prices:
      if price < min_price:
        min_price = price
      
      if price - min_price > max_profit:
        max_profit = price - min_price
      
    return max_profit

TestSolution().maxProfit()

