class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:   
        found = {}
        len_nums = len(nums)

        for i in range(1, len_nums + 1):
            found[i] = 1

        for num in nums:
            found[num] = 0

        return [key for key, val in found.items() if val == 1] 