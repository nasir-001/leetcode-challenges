class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for word in strs:
            sortedwords = "".join(sorted(word))

            if sortedwords not in dict:
                dict[sortedwords] = [word]
            else:
                dict[sortedwords].append(word)

        result = []
        for val in dict.values():
            result.append(val)
        
        return result