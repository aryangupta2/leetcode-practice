class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        s = s.replace(" ", "")

        i = 0
        j = len(s) - 1
        
        while i < j:

            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if not s[i].isalnum():
                    i += 1
                elif not s[j].isalnum():
                    j -= 1
                else:
                    return False

        return True