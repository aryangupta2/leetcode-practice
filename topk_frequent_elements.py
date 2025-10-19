class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if len(nums) == 1:
            return nums
        
        occurrences = {}
        output = []

        for num in nums:
            if num in occurrences:
                occurrences[num] += 1
            else:
                occurrences[num] = 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in occurrences.items():
            buckets[freq].append(num)

        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                output.append(num)
                if len(output) == k:
                    return output