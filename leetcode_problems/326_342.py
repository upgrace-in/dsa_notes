# Power of Three and Four
# Return true if the given number is a power of 3 or 4

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n >= 3:
            if n % 3 != 0:
                return False
            n = n/3
        return n == 1
    
    def isPowerOfFour(self, n: int) -> bool:
        while n >= 4:
            if n % 4 != 0:
                return False
            n = n/4
        return n == 1

s = Solution().isPowerOfThree(27)
print(s)

s = Solution().isPowerOfFour(64)
print(s)