class Solution:
    def maxArea(self, heights: List[int]) -> int:
        storage = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            minH = min(heights[left], heights[right])
            CurrStorage = minH * (right - left)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

            if CurrStorage > storage:
                storage = CurrStorage

        return max(storage, 0)
