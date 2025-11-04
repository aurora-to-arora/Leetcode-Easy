class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False  
        reverse = 0
        temp = x
        while temp:
            reverse = reverse * 10 + (temp % 10)
            temp //= 10
        return x == reverse

#Time complexity - O(log₁₀ x)
#Each iteration removes one digit from temp.
#So the number of iterations = number of digits in x.
