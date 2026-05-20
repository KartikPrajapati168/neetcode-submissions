class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted1="".join(sorted(s))
        print(sorted1)
        sorted2="".join(sorted(t))
        print(sorted2)
        if sorted1==sorted2:
            return True
        else:
            return False