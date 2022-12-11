# Time complexity: O(n)
# Space complexity: O(1)
from typing import List

class TestSolution:
  def maxProduct(self):
    solution = Solution()
    assert solution.maxProduct([2,3,-2,4]) == 6
    assert solution.maxProduct([-2,0,-1]) == 0
    assert solution.maxProduct([-2,3,-4]) == 24
    assert solution.maxProduct([-2]) == -2
    assert solution.maxProduct([0,2]) == 2
    assert solution.maxProduct([0,2,4,0,1,-1,5]) == 8
    assert solution.maxProduct([3,-1,4]) == 4
    assert solution.maxProduct([2,-5,-2,-4,3]) == 24

class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    res = max(nums)
    curMin, curMax = 1, 1

    for num in nums:
      tmpMax = curMax * num
      curMax = max(tmpMax, num * curMin, num)
      curMin = min(tmpMax, num * curMin, num)
      res = max(res, curMax)
    
    return res

TestSolution().maxProduct()
