class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagram = defaultdict(list) # convert to dict
        for s in strs:
            sorted_s = ''.join(sorted(s)) # sort every word in the list
            group_anagram[sorted_s].append(s) # append in specific list if anagrams
        return list(group_anagram.values()) # creturn values because it is a dict