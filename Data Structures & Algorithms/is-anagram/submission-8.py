class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        if len(s) != len(t):
            print("====================")
            return False
        for i in s.lower():
            dict[i] = dict.get(i,0) + 1
        
        for i in t.lower():
            dict[i] = dict.get(i,0) - 1
            if dict[i] < 0:
                return False
        return True
        