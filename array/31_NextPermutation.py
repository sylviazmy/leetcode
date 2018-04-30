class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        replace1 = 0
        flag = False
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                replace1 = i
                flag = True
                break
        replace2 = replace1 + 1
        for j in range(replace1 + 1, len(nums)):
            if nums[j] < nums[replace1 + 1] and nums[j] > nums[replace1]:
                replace2 = j
        if not flag:
            nums[::] = nums[::-1]
        else:
            nums[replace1], nums[replace2] = nums[replace2], nums[replace1]
            nums[replace1 + 1:] = sorted(nums[replace1 + 1:])
























