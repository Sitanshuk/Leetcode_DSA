#  Max Consecutive Ones III

"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        curr = 0
        max_len = 0
        l = 0
        for r, num in enumerate(nums):
            if num == 0:
                curr += 1
            
            while curr > k and l<=r:
                if nums[l] == 0:
                    curr -= 1
                l += 1
            curr_max = r - l + 1
            max_len = max(curr_max, max_len)

        return max_len        
                
        
# Runtime beats 45% of leetcode submissions in Python
# Memory usage beats 43% of leetcode submissions in Python