#https://neetcode.io/problems/merge-strings-alternately/history?submissionIndex=4

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = [] 
        k = min(len(word1), len(word2))
        
        for i in range(k): 
            result.append(word1[i])
            result.append(word2[i])

        if k < len(word1):
            result.append(word1[k:])
        if k < len(word2):
            result.append(word2[k:])
        
        return "".join(result)