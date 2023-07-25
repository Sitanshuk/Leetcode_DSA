#  Longest Substring Without Repeating Characters

"""
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        max_len = 0
        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
            else:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1
            max_len = max(r-l+1, max_len)
        
        return max_len
        

# Runtime beats 80% of leetcode submissions in Python
# Memory usage beats 50% of leetcode submissions in Python