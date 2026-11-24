class Solution:
    def heapify(self,nums,n,i):
        largest = i
        left = 2*i+1
        right = 2*i+2

        #check left child
        if left < n and nums[left] > nums[largest]:
            largest=left
        #check right child
        if right < n and nums[right] > nums[largest]:
            largest=right
        #swap if child is greater
        if largest!=i:
            nums[i],nums[largest]=nums[largest],nums[i]

            #heapify affected subtree
            self.heapify(nums,n,largest)
            
    def buildMaxHeap(self,nums):
        n=len(nums)

        #Build Max Heap
        for i in range(n//2-1,-1,-1):
            self.heapify(nums,n,i)
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)

        self.buildMaxHeap(nums)

        for i in range(n-1,0,-1):
            nums[0],nums[i] = nums[i],nums[0]
            self.heapify(nums,i,0)

        return nums
        


