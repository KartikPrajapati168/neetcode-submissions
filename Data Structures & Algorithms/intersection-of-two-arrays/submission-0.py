class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i=0
        j=0
        arr=[]
        while i<len(nums1):
            while j<len(nums2):
                if nums1[i]!=nums2[j]:
                    j+=1
                else:
                    if nums2[j] not in arr:
                        arr.append(nums2[j])
                    j+=1
            j=0
            i+=1
            
        return arr