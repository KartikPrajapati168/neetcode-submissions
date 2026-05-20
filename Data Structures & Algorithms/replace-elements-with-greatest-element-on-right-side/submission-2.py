class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        for i in range(n):
            maxi = -1
            for j in range(i+1, n):
                if arr[j] > maxi:
                    maxi = arr[j]
            arr[i] = maxi
        return arr