class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        result = maxSum
        for i in range(1, len(nums)):
            maxSum = max(nums[i], nums[i] + maxSum)
            result = max(result, maxSum)

        return result
