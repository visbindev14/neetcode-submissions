class Solution:
    def isPalindrome(self, s: str) -> bool:
        parsed_str = "".join(i.lower() for i in s if i.isdigit() or i.isalpha())
        l, r = 0, len(parsed_str) - 1
        while l < r:
            if parsed_str[l] == parsed_str[r]:  
                l+=1
                r-=1
            else:
                return False
        #     return False
        return True
            
        
        
        