class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        best = -1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]<=nums[-1]:
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        return nums[best]
        