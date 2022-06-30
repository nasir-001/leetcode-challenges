from typing import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        s_counter = Counter(s)

        for char, num in t_counter.items():
            if char not in s_counter or num != s_counter[char]:
                return char


obj = Solution()

print(obj.findTheDifference('abcd', 'abcd'))

# Solution 2
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return list(Counter(t) - Counter(s))[0]