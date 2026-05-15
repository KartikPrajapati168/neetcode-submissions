class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check=set()
        n=len(nums)
        for i in range(n):
            if nums[i] not in check:
                check.add(nums[i])
            else:
                return True
        return False