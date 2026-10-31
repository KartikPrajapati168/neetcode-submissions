class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left=0
        window_sum=0
        result=1
        right=0
        for right in range(len(nums)):
            window_sum = window_sum + nums[right]
            
            while (nums[right]*(right-left+1)-window_sum) > k:
                window_sum = window_sum - nums[left]
                left=left+1
                
            window_size = right-left+1
            result=max(result,window_size)
            
        return result