class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        final_count = 0
        odd_is_present = False
        for char in char_count:
            if char_count[char] % 2 == 0:
                final_count += char_count[char]
            else:
                final_count += (char_count[char] -1)
                odd_is_present = True
        if odd_is_present:
            final_count += 1

        return final_count