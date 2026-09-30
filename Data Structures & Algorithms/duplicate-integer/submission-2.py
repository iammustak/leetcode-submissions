class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:
         
        a=set()
        for i in nums:
            a.add(i)

        if len(nums)!=len(a):
            return True
        return False   
