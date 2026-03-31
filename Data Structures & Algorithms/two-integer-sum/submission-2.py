class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in nums and nums.index(diff) != i:
                return sorted([i, nums.index(diff)])