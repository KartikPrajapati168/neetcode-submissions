class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if k==1:
            return 0
        nums.sort()
        ans=float('inf')
        for right in range(k-1,n):
            left=right-k+1
            difference=nums[right]-nums[left]
            ans=min(ans,difference)
        
        return ans