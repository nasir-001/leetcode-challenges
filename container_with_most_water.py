class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left 
            minHeight = min(height[left], height[right])
            maxArea = max(maxArea, (width * minHeight))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea