class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n=len(arr)
        sum=0
        count=0
        i=0
        for j in range(k):
            sum=sum+arr[j]
        avg=sum/k
        if avg>=threshold:
            count=count+1
        j=j+1
        while j<n:
            sum=sum+arr[j]
            sum=sum-arr[i]
            avg=sum/k

            if avg>=threshold:
                count=count+1
            j=j+1
            i=i+1
        return count