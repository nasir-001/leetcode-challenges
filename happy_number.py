class Solution:
    def isHappy(self, n: int) -> bool:
        def squareSum(num):
            result = 0

            while num > 0:
                remainder = num % 10
                result = result + remainder * remainder
                num = num // 10

            return result

        
        seen = set()
        while squareSum(n) not in seen:
            sum1 = squareSum(n)
            if sum1 == 1:
                return True
            else:
                seen.add(sum1)
                n = sum1

        return False
                