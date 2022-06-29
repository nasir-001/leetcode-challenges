class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stripped = list(s.strip().split(" "))

        return len(stripped[-1])
