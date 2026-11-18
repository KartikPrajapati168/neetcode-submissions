class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i=0
        if n == 0:
            return True
        while i < len(flowerbed):
            left_empty = (i==0 or flowerbed[i-1]==0)
            right_empty = (i==len(flowerbed)-1 or flowerbed[i+1]==0)
            current_empty = (flowerbed[i]==0)

            if left_empty and right_empty and current_empty:
                flowerbed[i]=1
                n-=1

            if n==0:
                return True

            i+=1

        return False
    