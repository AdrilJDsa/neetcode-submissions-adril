class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = []
        add = 0
        for i in nums:
            if i == 0:
                count.append(add)
                add = 0
            else:
                add += 1
        count.append(add)
        return max(count)
        