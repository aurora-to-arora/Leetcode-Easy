class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        rev = 0
        n = x
        while n:
            r= n%10
            rev=rev*10+r
            n=n//10
        return x==rev
        
