# Time complexity: O(n)
# Space complexity: O(1)
from typing import List

class TestSolution:
  def maxSubArray(self):
    solution = Solution()
    assert solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert solution.maxSubArray([1]) == 1
    assert solution.maxSubArray([-1]) == -1
    assert solution.maxSubArray([-2, 1]) == 1
    assert solution.maxSubArray([-1, -2]) == -1
    assert solution.maxSubArray([-2,-3,-1]) == -1
    assert solution.maxSubArray([5,4,-1,7,8]) == 23
    assert solution.maxSubArray([5,4,-1,7,8,-20,10,-20,10,5,3]) == 23
    assert solution.maxSubArray([5,4,-1,7,-20,10,-20,10,5,3]) == 18


class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    max_profit = current_profit = nums[0]
    
    for i in range(1, len(nums)):
      current_profit = max(current_profit + nums[i], nums[i])
      max_profit = max(max_profit, current_profit)
    
    return max_profit

TestSolution().maxSubArray()
