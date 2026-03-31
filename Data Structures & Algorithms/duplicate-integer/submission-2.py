class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # set_num = set(nums)
        # if len(set_num) < len(nums):
        #     return True
        # else:
        #     return False
        # # ORRR

        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        
         

        