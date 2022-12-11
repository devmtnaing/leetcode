# Time complexity: O(log n)
# Space complexity: O(1)
from typing import List

class TestSolution:
  def findMin(self):
    solution = Solution()
    assert solution.findMin([3,4,5,1,2]) == 1
    assert solution.findMin([4,5,6,7,0,1,2]) == 0
    assert solution.findMin([11,13,15,17]) == 11
    assert solution.findMin([1]) == 1
    assert solution.findMin([2,1]) == 1

class Solution:
  def findMin(self, nums: List[int]) -> int:
    if len(nums) == 1:
      return nums[0]

    low = 0
    high = len(nums) - 1

    while low <= high:
      mid = (low + high) // 2
      if nums[mid+1] < nums[mid]:
        return nums[mid+1]
      
      if nums[mid] < nums[mid-1]:
        return nums[mid]
      
      if nums[high] < nums[mid]:
        low = mid + 1
      else:
        high = mid - 1

TestSolution().findMin()
