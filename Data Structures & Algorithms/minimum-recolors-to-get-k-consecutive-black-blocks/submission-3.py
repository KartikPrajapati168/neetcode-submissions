class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        string=""
        white_count=0
        min_operations=float('inf')
        for i in range(len(blocks)-k+1):
            # Number of windows = n -k + 1
            string=blocks[i:i+k]
            white_count=string.count("W")
            min_operations=min(min_operations,white_count)
            
        return min_operations    