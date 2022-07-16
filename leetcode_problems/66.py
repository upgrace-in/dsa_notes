from re import S


class Solution:
    def plusOne(self, digits):
        digit = ''.join(str(x) for x in digits)
        return [int(x) for x in str(int(digit)+1)]

s = Solution()
print(s.plusOne([1,2,3]))