# https://neetcode.io/problems/is-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_set_s = {}

        for char in s: 
            if char in freq_set_s: 
                freq_set_s[char] += 1 
            else:
                freq_set_s[char] = 1 
        
        for char in t: 
            if char not in freq_set_s:
                return False 
            else: 
                freq_set_s[char] -= 1 
            
        for char in freq_set_s: 
            if freq_set_s[char] != 0: 
                return False 
        
        return True 