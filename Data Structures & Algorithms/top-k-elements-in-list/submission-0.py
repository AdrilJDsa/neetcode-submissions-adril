class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countK = {}
        klist = []
        for i in range(len(nums)):
            countK[nums[i]] = 1 + countK.get(nums[i], 0)
        
        # Sort the keys based on their frequency (values in countK) in descending order
        sorted_keys = sorted(countK.keys(), key=lambda x: countK[x], reverse=True)
        
        # Take the first k elements from the sorted list
        return sorted_keys[:k]