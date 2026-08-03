from collections import defaultdict
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        window_sum = 0
        largest = 0
        for i in range(k):
            window_sum += nums[i]
            freq[nums[i]] += 1
        if len(freq) == k:
            largest = window_sum
        for r in range(k, len(nums)):
            l = r - k
            window_sum -= nums[l]
            freq[nums[l]] -= 1
            if freq[nums[l]] == 0:
                del freq[nums[l]]

            window_sum += nums[r]
            freq[nums[r]] += 1
            if len(freq) == k:
                largest = max(largest, window_sum)

        return largest
