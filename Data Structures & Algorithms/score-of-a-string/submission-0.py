class Solution:
    def scoreOfString(self, s: str) -> int:
        left=0
        right=1
        final_score=0
        while right<len(s):
            final_score=final_score+abs(ord(s[right])-ord(s[left]))
            left=left+1
            right=right+1
        return final_score