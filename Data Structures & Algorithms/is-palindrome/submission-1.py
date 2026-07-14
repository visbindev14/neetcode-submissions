class Solution:
    def isPalindrome(self, s: str) -> bool:
        parsed_str = "".join(i.lower() for i in s if i.isdigit() or i.isalpha())
        if parsed_str == parsed_str[::-1]:
            return True
        return False
            
        
        
        