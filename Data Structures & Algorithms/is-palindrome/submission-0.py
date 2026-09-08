class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        cleaned = [ch.lower() for ch in s if ch.isalnum()]
        
        stack = []
   
        for ch in cleaned:
            stack.append(ch)
        
    
        for ch in cleaned:
            if ch != stack.pop():
                return False
        return True