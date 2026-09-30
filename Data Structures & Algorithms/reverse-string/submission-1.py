class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.


        """
        sta=[]
        for i in s:
            sta.append(i)
        for i in range(len(s)):
            s[i]=sta.pop()    
    
        