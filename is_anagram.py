class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        char_counts = {}

        for char in s:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
        
        for char in t:
            if char in char_counts:
                char_counts[char] -= 1

        return all(value == 0 for value in char_counts.values())
        