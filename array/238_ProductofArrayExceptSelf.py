class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        curRes=[1]*len(nums)
        for i in range(1,n):
            curRes[i]=curRes[i-1]*nums[i-1]

        for j in range(n-2,-1,-1):
            curRes[j]=curRes[j]*nums[j+1]
            nums[j]=nums[j]*nums[j+1]

        return curRes