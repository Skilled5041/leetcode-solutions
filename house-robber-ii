class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        case1Prev2 = 0
        case1Prev1 = 0

        for i in range(len(nums) - 1):
            curr = max(case1Prev1, case1Prev2 + nums[i])
            case1Prev2 = case1Prev1
            case1Prev1 = curr

        case2Prev2 = 0
        case2Prev1 = 0

        for i in range(1, len(nums)):
            curr = max(case2Prev1, case2Prev2 + nums[i])
            case2Prev2 = case2Prev1
            case2Prev1 = curr

        return max(case2Prev1, case1Prev1)
