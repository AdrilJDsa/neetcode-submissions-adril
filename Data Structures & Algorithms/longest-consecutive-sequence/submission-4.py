class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))

        if not nums:
            return 0

        l = len(nums)
        n = nums[0]
        count = 1
        new_count = 1

        for i in range(1, l):
            if nums[i] != n + 1:
                new_count = max(count, new_count)
                count = 1
                n = nums[i]
            else:
                count += 1
                n += 1

        new_count = max(count, new_count)
        return new_count