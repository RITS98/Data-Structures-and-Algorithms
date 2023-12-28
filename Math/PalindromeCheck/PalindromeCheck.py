class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if x>=0 and x<=9:
            return True
        
        if x%10 == 0:
            return False
        
        reverse = 0
        temp = x
        
        while temp > 0 :
            
            reverse = reverse*10 + temp%10
            temp = temp//10
            
        return reverse == x