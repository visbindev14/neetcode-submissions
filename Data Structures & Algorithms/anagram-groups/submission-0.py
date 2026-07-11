class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for i in strs:
            if tuple(sorted(i)) not in dict:
                dict[tuple(sorted(i))] = []
            dict[tuple(sorted(i))].append(i)
        
        return list(dict.values())
        