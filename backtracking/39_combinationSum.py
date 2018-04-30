class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        self.dfs(candidates, target, 0, res, [])
        return res

    def dfs(self, candidates, target, curSum, res, curL):
        if curSum == target:
            res.append(curL)
        elif curSum < target:
            for j in range(len(candidates)):
                self.dfs(candidates[j:], target, curSum + candidates[j], res, curL + [candidates[j]])

