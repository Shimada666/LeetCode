class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for i in range(1, length):
            subMaxSum = max(nums[i] + nums[i - 1], nums[i])
            nums[i] = subMaxSum
        return max(nums)
