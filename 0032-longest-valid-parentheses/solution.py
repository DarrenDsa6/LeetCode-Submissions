class Solution(object):
    def longestValidParentheses(self, s):
        stack = []
        max_len = 0
        last_invalid_index = -1
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        max_len = max(max_len, i - stack[-1])
                    else:
                        max_len = max(max_len, i - last_invalid_index)
                else:
                    last_invalid_index = i  
        return max_len

