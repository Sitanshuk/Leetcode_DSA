#  Check if the Sentence Is Pangram

"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false
 

Constraints:

1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
"""

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sent_set = set(sentence)
        for i in range(26):
            letter = chr(ord('a') + i)
            
            #This is O(1) operation as opposed to O(n) because lookups in set in O(1)
            if letter not in sent_set:
                return False
        return True

# Runtime beats 50% of leetcode submissions in Python
