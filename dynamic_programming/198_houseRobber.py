class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur, maxP_3step_before, max_2step_before = 0, 0, 0#initiate the arguments, it will be used for loop
        for i in range(len(nums)):
            nums[i] = max(maxP_3step_before, max_2step_before) + nums[i]
            max_3step_before, max_2step_before, cur = max_2step_before, cur, max(cur, nums[i])
        return cur

