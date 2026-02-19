# https://neetcode.io/problems/valid-palindrome-ii/history?submissionIndex=1
class Solution:
    def validPalindrome(self, s: str) -> bool: #abc
        def is_pal(i: int, j: int) -> bool: 
            while i < j: 
                if s[i] != s[j]:
                    return False 
                i += 1 
                j -= 1 
            return True 
        
        left, right = 0, len(s)-1 
        while left < right: 
            if s[left] == s[right]:
                left += 1 
                right -= 1 
            else: 
                return is_pal(left + 1, right) or is_pal(left, right - 1)
        
        return True 
        