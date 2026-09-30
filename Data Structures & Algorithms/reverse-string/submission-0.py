class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        
        """
        stac=[]

        for i in s:
            stac.append(i)
        i=0
        while stac:
            s[i]=stac.pop()    
            i+=1
        return stac    
        