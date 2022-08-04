class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        prevMap = {}
        bools = None
        
        for i, n in enumerate(nums):
            if n in prevMap:
                bools = True
            prevMap[n] = i
            
        return bools