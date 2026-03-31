class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anamap = defaultdict(list)
        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c) - ord("a")] += 1
            
            anamap[tuple(count)].append(word)
        return list(anamap.values())