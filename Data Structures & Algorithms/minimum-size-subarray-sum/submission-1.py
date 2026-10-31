class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum=float('inf')
        sum=0
        j=0
        n=len(nums)
        i=0
        while j<n:
            sum=sum+nums[j]
            while sum >= target:
                minimum=min(minimum,j-i+1)
                sum=sum-nums[i]
                i+=1
            j+=1
        
        if minimum == float('inf'):
            return 0
        return minimum