# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         output = []
#         for i in range(len(nums)):
#             count = 0
#             for j in range(len(nums)):
#                 if j != i and nums[j] < nums[i]:
#                     count += 1
#             output.append(count)

#         return output

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smaller_dict = {}
        sorted_nums = sorted(nums, reverse=True)
        for i in range(len(sorted_nums) - 1):
            curr_num = sorted_nums[i]
            next_num = sorted_nums[i+1]
            if next_num < curr_num:
                remaining_values = len(sorted_nums) - (i + 1)
                smaller_dict[curr_num] = remaining_values

        smaller_dict[sorted_nums[-1]] = 0

        output = []
        for num in nums:
            output.append(smaller_dict[num])

        return output
