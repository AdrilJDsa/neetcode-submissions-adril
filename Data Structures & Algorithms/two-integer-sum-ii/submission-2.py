class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        second = len(numbers) - 1
        sum_fs = 0
        while first < second:
            sum_fs = numbers[first] + numbers[second]
            if sum_fs == target:
                print(first, second)
                return [first+1, second+1]
            elif sum_fs > target:
                second -= 1
            else:
                first += 1
        return []