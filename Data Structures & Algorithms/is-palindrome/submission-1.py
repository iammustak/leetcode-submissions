class Solution:
    def isPalindrome(self,s):
        stra=""
        for i in s:
            if i.isalnum():
                stra+=i.lower()
        return stra==stra[::-1]        

    
        