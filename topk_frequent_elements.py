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

        for i in range(k):
            max_occurrence = max(occurrences.values())
            key_to_remove = None

            for k, v in occurrences.items():
                if v == max_occurrence:
                    output.append(k)
                    key_to_remove = k
                    break

            if key_to_remove is not None:
                del occurrences[key_to_remove]

        return output