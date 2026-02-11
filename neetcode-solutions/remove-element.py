class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # traverse nums, pop nums[i] if nums[i] == val 
        # traverse nums again, return len(nums)

        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)