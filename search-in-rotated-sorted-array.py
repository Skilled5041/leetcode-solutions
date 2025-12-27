class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findOffset(nums, l, r):
            while l != r:
                mid = l + (r - l) // 2
                if nums[mid] > nums[-1]:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        def binarySearch(nums, target, l, r):
            offset = findOffset(nums, 0, len(nums) - 1)
            while l <= r:
                mid = l + (r - l) // 2
                offsetMid = (mid + offset) % len(nums)

                if nums[offsetMid] == target:
                    return offsetMid
                elif nums[offsetMid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        return binarySearch(nums, target, 0, len(nums) - 1)
