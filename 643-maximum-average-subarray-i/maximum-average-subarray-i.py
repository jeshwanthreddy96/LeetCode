class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        l=0
        r=0
        s=0.0
        av=0.00
        avg=[]
        while r<len(nums):
            s+=nums[r]
            if r-l+1 == k:
                av = s/k
                avg.append(av)
                s-=nums[l]
                l+=1
            r+=1
        return max(avg)