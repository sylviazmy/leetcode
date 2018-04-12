# Given a collection of distinct numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(len(nums)):
            self.dfs(nums[i], nums[:i] + nums[i + 1:], ans, [nums[i]])
        return ans

    def dfs(self, root, nums, ans, permu):

        if not nums:
            ans.append(permu)
        else:
            for i in range(len(nums)):
                self.dfs(nums[i], nums[:i] + nums[i + 1:], ans, permu + [nums[i]])