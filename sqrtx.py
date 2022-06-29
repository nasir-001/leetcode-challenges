import math

class Solution:
    def mySqrt(self, x: int) -> int:
        return "%d"%(math.sqrt(x))

obj = Solution()
print(obj.mySqrt(8))