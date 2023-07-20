#  Maximum Average Subarray I

"""

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104

"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_val = 0
    
        for i in range(k):
            sum_val += nums[i]
        max_val = sum_val
        for i in range(k, len(nums)):
            sum_val = sum_val + nums[i] - nums[i-k]
            max_val = max(sum_val, max_val)

        return max_val/k
            

 # Runtime beats 71% of leetcode submissions in Python
 # Memory usage beats 98% of leetcode submissions in Python