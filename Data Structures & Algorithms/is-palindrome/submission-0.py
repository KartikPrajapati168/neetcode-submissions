class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        new_s2=""
        for ch in s.lower():
            if ch.isalnum():
                new_s2=new_s2+ch

        j=len(new_s2)-1
        while i<j:
            if new_s2[i]!=new_s2[j]:
                return False
            i=i+1
            j=j-1
        return True