class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagram = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            group_anagram[sorted_s].append(s)
        return list(group_anagram.values())