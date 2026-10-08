class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        s = list(s)
        swaps = 0

        for i in range(len(s)):

            if s[i] == "]":
                balance -= 1
            else:
                balance += 1

            if balance < 0:

                j = len(s) -1

                while s[j] != "[":
                    j -=1

                s[i], s[j] = s[j], s[i]

                balance += 2
                swaps += 1

        return swaps