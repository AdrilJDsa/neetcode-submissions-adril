class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        i = len(stones)
        while(i > 1):
            s1_i = stones.index(max(stones))
            stone1 = stones.pop(s1_i)
            s2_i = stones.index(max(stones))
            stone2 = stones.pop(s2_i)
            print(stone1, stone2)
            if stone1 == stone2:
                print(stone1, stone2)
                i -= 2
            else:
                new_stone = abs(stone1 - stone2)
                stones.append(new_stone)
                i -= 1
            print(stones)


        if i == 0:
            return 0
        else:
            return stones[i-1]
        