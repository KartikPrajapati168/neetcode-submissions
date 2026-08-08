class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result_str=""
        i=0
        j=0
        while i<len(word1) and j<len(word2):
            adding=word1[i]+word2[j]
            result_str=result_str+adding
            i=i+1
            j=j+1

        while i<len(word1):
            result_str=result_str+word1[i]
            i=i+1

        while j<len(word2):
            result_str=result_str+word2[j]
            j=j+1
        return result_str