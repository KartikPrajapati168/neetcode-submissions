class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique=set()
        left=0
        max_length=0
        for i in range(len(s)):
            while s[i] in unique:
                unique.remove(s[left])
                left+=1
                
            unique.add(s[i])    
            max_length=max(max_length,i-left+1)
        
        return max_length   