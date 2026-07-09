class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result=[]
        '''for j in range(len(nums)-2):
            key = nums[j]
            for i in range(j+1,len(nums)-1):
                if (key+nums[i]+nums[i+1])==0:
                    if [key,nums[i],nums[i+1]] not in result:
                    result.append([key,nums[i],nums[i+1]])'''
        nums.sort()
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left<right:
                total = nums[i]+nums[left]+nums[right]
                if total == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif total<0:
                    left+=1
                else:
                    right-=1
        return result

