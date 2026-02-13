# https://neetcode.io/problems/majority-element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = float('-inf') 
        count = 0 
        for num in nums:
            if candidate == float('-inf'): 
                candidate = num 
                count += 1 
            if count == 0:
                candidate = num 
                count += 1 
            elif candidate == num:
                count += 1 
            elif candidate != num: 
                count -= 1

        
        return candidate