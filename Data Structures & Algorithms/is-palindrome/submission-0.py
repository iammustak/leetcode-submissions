class Solution:
    def isPalindrome(self, s: str) -> bool:
        stri=""
        for i in s:
            if i.isalnum():
                stri+=i.lower()
        return stri==stri[::-1]        


    
        