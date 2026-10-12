class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        m={}
        for i in range(len(nums)):
            if nums[i] in m:
                m[nums[i]]+=1
            else:
                m[nums[i]]=1
        
        for key in m:
            if m[key]>len(nums)//2:
                return key