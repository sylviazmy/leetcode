class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(1, n + 2 - k):
            self.dfs(i + 1, n + 2 - k, [i], res, k)
        return res

    def dfs(self, l, r, cur, res, k):
        if len(cur) == k:
            res.append(cur)
        else:
            for j in range(l, r + 1):
                # print(j, l, r + 1)
                self.dfs(j + 1, r + 1, cur + [j], res, k)#注意，用dfs的时候不要给参数做任何修改，全都在递归的时候进行修改


