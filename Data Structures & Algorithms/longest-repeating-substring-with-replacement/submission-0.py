class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        
        left=0
        max_freq=0
        result=0
        
        count=[0]*26
        
        for right in range(n):
            
            #Step 1: Current character ki frequency increase karo 
            index=ord(s[right])-ord('A') 
            count[index]+=1
            
            #Step 2: Maximum frequency update karo 
            max_freq=max(max_freq,count[index]) # 1 2 3 4 #3 #4 #4
            
            #Step 3: Check karo window valid hai ya nahi
            window_length=right-left+1 #1-0+1=2 2-0+1  #4 #4-0+1 #6 #6-1+1
            
            if window_length - max_freq > k:
                #Step 4:Left character ko window se remove karo
                left_index=ord(s[left])-ord('A')
                count[left_index]-=1
                
                #Step 5:Left pointer aage badhao
                left+=1
                
            #Step 6: Maximum valid window update karo 
            result = max(result,right-left+1)
        
        return result