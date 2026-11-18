class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)

        answer=high
        while low<=high:
            mid=(low+high)//2

            current_sum=0
            count=1

            #Greedy: count required subarrays
            for num in nums:
                if current_sum+num <= mid:
                    current_sum+=num
                else:
                    count+=1
                    current_sum=num

            #Binary search decision
            if count <= k:
                answer=mid
                high=mid-1
            else:
                low=mid+1

        return answer
