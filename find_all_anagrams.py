class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        string_s_length, string_p_length = len(s), len(p)

        if string_s_length < string_s_length:
            return []

        p_count = Counter(p)
        s_count = Counter()

        result = []
        for i in range(string_s_length):
            s_count[s[i]] += 1
            if i >= string_p_length:
                if s_count[s[i - string_p_length]] == 1:
                    del s_count[s[i - string_p_length]]
                else:
                    s_count[s[i - string_p_length]] -= 1
            if p_count == s_count:
                result.append(i - string_p_length + 1)

        return result
