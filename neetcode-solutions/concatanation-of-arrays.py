# https://neetcode.io/problems/concatenation-of-array/question

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = [None] * (len(nums) * 2)
        i = 0 

        for i in range(len(nums)):
            result[i] = nums[i]
            i += 1

        j = i
        for j in range(len(nums)*2):
            result[j] = nums[j-len(nums)]

        return result
