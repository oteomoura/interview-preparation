class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_table = {}

        for num in nums: 
            if num not in freq_table: 
                freq_table[num] = 1 
            else:
                freq_table[num] += 1 

        for key in freq_table.keys(): 
            if freq_table[key] > 1: 
                return True 
        
        return False 