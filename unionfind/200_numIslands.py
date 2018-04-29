class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    count += 1
        return count

    def bfs(self, grid, i, j):
        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] != '1':
            return
        grid[i][j] = "-1"
        self.bfs(grid, i, j + 1)
        self.bfs(grid, i + 1, j)
        self.bfs(grid, i - 1, j)
        self.bfs(grid, i, j - 1)
        return grid



