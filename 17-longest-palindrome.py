#https://leetcode.com/problems/longest-palindrome
class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}
        for char in s:
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1

        result = 0
        odd_char_count = 0
        for char in letters:
            occurrence_count = letters[char]
            if occurrence_count > 1:
                if occurrence_count % 2 == 0:
                    result += occurrence_count
                else:
                    result += occurrence_count - 1
                    odd_char_count += 1
            else:
                odd_char_count += 1

        if odd_char_count > 0:
            result +=1

        return result
