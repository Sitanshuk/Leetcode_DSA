#  Ransom Note

"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_count = dict()
        m_count = dict()
        for ch in ransomNote:
            r_count[ch] = r_count.get(ch, 0) + 1
        for ch in magazine:
            m_count[ch] = m_count.get(ch, 0) + 1
        for ch in r_count:
            if r_count[ch] > m_count.get(ch, 0):
                return False
        return True
            
            
# Runtime beats 42% of leetcode submissions in Python
# Memory usage beats 67% of leetcode submissions in Python