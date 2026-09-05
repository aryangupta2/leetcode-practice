class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_all_nums = sum(range(len(nums) + 1))
        sum_nums = sum(nums)

        return sum_all_nums - sum_nums
