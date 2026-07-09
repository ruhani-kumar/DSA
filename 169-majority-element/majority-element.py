class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''max = 0
        for x in nums:
            if nums.count(x)>max:
                max = nums.count(x)
                result = x

        return result'''
        n= len(nums)
        count= Counter(nums)
        for num, fr in count.items():
            if fr> n/2:
                return num
