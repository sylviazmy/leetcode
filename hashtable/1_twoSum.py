class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        easy
        """
        dic={}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[target-nums[i]]=i
            else:
                return [dic[nums[i]],i]
