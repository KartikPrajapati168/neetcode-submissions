class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        while i<len(nums): #0<3 #1<3
            # print(i)
            for j in range(i+1,len(nums)): #1 2
                if nums[i]==nums[j] and abs(i-j)<=k: #2==1 #2==2
                    return True
            i=i+1
        return False