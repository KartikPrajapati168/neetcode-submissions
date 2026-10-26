class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen=set()
        result=set()
        n=len(s)
        string=""
        if n<10:
            return []
        else:
            for i in range(n-9):
                string=s[i:i+10]
                
                if string not in seen:
                    seen.add(string)
                else:
                    result.add(string)
                    
        return list(result)