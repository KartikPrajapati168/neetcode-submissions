class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left=0
        result=[]
        while left < len(nums):
            right=left+1
            while right<len(nums):
                if nums[left]+nums[right]==target:
                    result.extend([left,right])
                right=right+1
            left=left+1
        return result