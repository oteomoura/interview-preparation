# https://neetcode.io/problems/two-integer-sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for each num in nums, calc diff = target - nums[i]
        # build diff_map = { diff: position }
        # for each j in nums, if diff_map[j], return [i, j]
        # [3, 4, 5, 6], target = 7
        diff_map = {}
        for index, value in enumerate(nums):
            diff = target - value # diff = 2, index = 2
            if value in diff_map:
                res = [diff_map[value], index]
                res.sort()
                return res
            diff_map[diff] = index   # diff_map = {4:0, 3:1}
