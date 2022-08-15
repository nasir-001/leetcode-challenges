class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        sLen = len(s)
        index = sLen - 1
        result = 0
        
        while index >= 0:
            if index < sLen - 1 and hashMap[s[index]] < hashMap[s[index + 1]]:
                result -= hashMap[s[index]]
            else:
                result += hashMap[s[index]]
                
            index -= 1
        return result