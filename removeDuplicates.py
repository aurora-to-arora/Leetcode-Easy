class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res=[]
        if not nums:
            return res
        j =0
        for i in range(1, len(nums)):
            if nums[j]!=nums[i]:
                j+=1
                nums[j]=nums[i]
        return j+1
        
