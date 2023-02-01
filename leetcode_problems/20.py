class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        dict1 = {"{": "}", "[": "]", "(": ")"}
        stack = []
        for i in range(len(s)):
            if s[i] in dict1.keys():
                stack.append(s[i])
            else:
                if len(stack) > 0:
                    last_item = stack.pop()
                    if s[i] != dict1[last_item]:
                        return False
                else:
                    return False

        return len(stack) == 0

s = Solution()
print(s.isValid("{[]}"))
