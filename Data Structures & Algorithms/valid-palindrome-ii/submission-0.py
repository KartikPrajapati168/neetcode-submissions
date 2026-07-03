class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s) - 1

        while left < right: #0<3 1<2

            if s[left] == s[right]: #a==a b==c
                left += 1  #b
                right -= 1 #c

            else:
                return (
                    isPalindrome(left + 1, right) or #2,3
                    isPalindrome(left, right - 1)
                )

        return True