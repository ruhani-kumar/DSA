class Solution:
    def rob(self, nums: List[int]) -> int:
        '''sumEven = 0
        sumOdd = 0
        for i in range(len(nums)):
            if i%2 == 0:
                sumEven += nums[i]
            else:
                sumOdd += nums[i]
        return max(sumOdd, sumEven)'''
        r1 = 0
        r2 = 0
        for n in nums:
            temp = max(r1+n, r2)
            r1 = r2
            r2 = temp
        return r2