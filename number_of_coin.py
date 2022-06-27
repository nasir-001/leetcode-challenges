class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sorted_piles = sorted(piles)
        end_index = len(piles) - 1
        our_value = 0
        for i in range(len(piles) // 3):
            our_value += sorted_piles[end_index-(i*2)-1]
        return our_value