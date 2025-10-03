class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        opening_parentheses = ["(", "[", "{"]
        parentheses = {")":"(", "]":"[", "}":"{"}

        parentheses_stack = [] 
        
        for char in s:
            if char in opening_parentheses:
                parentheses_stack.append(char)
            else:
                if not parentheses_stack:
                    return False
                
                if parentheses[char] == parentheses_stack[-1]:
                    parentheses_stack.pop()
                else:
                    return False
        
        return not parentheses_stack
