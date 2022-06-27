# class Solution:
#     def search(self, nums: List[int], target: int) -> int:

#         for i, num in enumerate(nums):
#             if num == target:
#                 return i
#         else:
#             return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            num = nums[mid]
            if target == num:
                return mid
            elif target > num:
                start = mid + 1
            elif target < num:
                end = mid - 1

        return -1