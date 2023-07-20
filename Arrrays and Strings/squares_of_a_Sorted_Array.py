#Squares of a Sorted Array
"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        num_sq = [0]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[l])>abs(nums[r]):
                num_sq[i] = nums[l]*nums[l]
                l += 1
            else:
                num_sq[i] = nums[r]*nums[r]
                r -= 1
        return num_sq
            
 # Runtime beats 75% of leetcode submissions in Python
 # Memory usage beats 70% of leetcode submissions in Python