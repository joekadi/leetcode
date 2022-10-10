#https://leetcode.com/problems/valid-anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChars = [*s]
        tChars = [*t]
        sChars.sort()
        tChars.sort()
        if sChars==tChars:
            return True
        else:
            return False
