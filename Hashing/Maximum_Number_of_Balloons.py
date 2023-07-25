#  Maximum Number of Balloons

"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_keys = set("balloon")
        balloon_vals = [0]*7
        balloon_counter = dict(zip(balloon_keys, balloon_vals))
        for char in text:
            if char in balloon_counter:
                balloon_counter[char] = balloon_counter[char] + 1
        
                
        balloon_counter['l'] //= 2
        balloon_counter['o'] //= 2
        return min(balloon_counter.values())
        
        
# Runtime beats 62% of leetcode submissions in Python
# Memory usage beats 72% of leetcode submissions in Python