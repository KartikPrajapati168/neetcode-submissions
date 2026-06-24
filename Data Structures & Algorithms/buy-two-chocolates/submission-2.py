class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        sum=prices[0]+prices[1]
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i]+prices[j]<sum:
                    sum=prices[i]+prices[j]
        return abs(sum-money) if sum<=money else money