class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        indices = {}

        for i in range(len(nums)):
            indices[nums[i]] = i

        for i in range(len(nums)): 
            complement = target - nums[i]
            if complement in indices and indices[complement] != i:
                return [i, indices[complement]]

        return []