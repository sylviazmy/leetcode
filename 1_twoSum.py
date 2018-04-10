class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                return [dic.get(target - nums[i]), i]
            else:
                dic[nums[i]] = i
        return []
