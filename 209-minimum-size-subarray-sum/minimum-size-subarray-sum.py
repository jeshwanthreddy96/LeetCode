class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = 0
        current_sum = 0
        min_length = float('inf')
        while r < len(nums):
            current_sum += nums[r]
            while current_sum >= target:
                current_length = r - l + 1
                min_length = min(min_length, current_length)
                current_sum -= nums[l]
                l += 1
            r += 1

        return min_length if min_length != float('inf') else 0
