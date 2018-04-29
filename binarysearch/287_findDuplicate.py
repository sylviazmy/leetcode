##use bi-search
#因为nums里数字是连续的1-n的数字，所以可以用mid来做一个分边
class Solution(object):
    def findDuplicate(nums):
        low = 1
        high = len(nums) - 1
        while low <= high:
            count = 0
            mid = (low + high) // 2
            print("mid is ", mid)
            for num in nums:
                if num <= mid:
                    count += 1
            if count <= mid:
                low = mid + 1
                print("low is ", low)
            else:
                high = mid - 1
                print("high is ", high)
        print(low)
        return low

#因为有重复数字出现，并且数字是从1到n，所以一定会形成环且不会超出边界
#设：链表头是X，环的第一个节点是Y，slow和fast第一次的交点是Z。各段的长度分别是a,b,c，如图所示。
#第一次相遇时slow走过的距离：a+b，fast走过的距离：a+b+c+b。

#因为fast的速度是slow的两倍，所以fast走的距离是slow的两倍，有 2(a+b) = a+b+c+b，可以得到a=c（这个结论很重要！）。

#ref: http://www.cnblogs.com/hiddenfox/p/3408931.html
class Solution2(object):
    def findDuplicate(nums):
        slow=fast=finder=0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:#第一次赶上相遇，但不一定就是形成环的节点
                while finder!=slow:#所以要继续遍历
                    finder=nums[finder]
                    slow=nums[slow]
                return finder



