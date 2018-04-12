# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        ans = []
        self.dfs(ans, n, n, "")
        return ans

    def dfs(self, ans, left, right, string):
        if left > right:
            return
        if left == 0 and right == 0:
            ans.append(string)
        if left > 0:
            self.dfs(ans, left - 1, right, string + "(")
        if right > 0:
            self.dfs(ans, left, right - 1, string + ")")
