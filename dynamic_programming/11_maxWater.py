class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxC = 0
        curC = 0
        l = 0
        r = len(height) - 1
        while l < r:
            curC = (r - l) * min(height[l], height[r])
            maxC = max(maxC, curC)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return maxC


