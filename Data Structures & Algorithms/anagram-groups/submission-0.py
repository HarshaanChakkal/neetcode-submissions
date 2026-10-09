class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for word in strs:
            sorted_word = "".join(sorted(word))  # Sort characters to create a key
            
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)  # Append to existing list
            else:
                anagram_dict[sorted_word] = [word]  # Create a new list
        
        return list(anagram_dict.values())

