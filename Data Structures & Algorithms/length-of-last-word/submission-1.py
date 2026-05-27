class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str_strip=s.strip(" ")
        str_split=str_strip.split(" ")[-1]
        print(len(str_split))
        return len(str_split)