class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0   # Pointer for word
        j = 0   # Pointer for abbreviation

        while i < len(word) and j < len(abbr):

            # Case 1: Current character is a letter
            if abbr[j].isalpha():

                if word[i] != abbr[j]:
                    return False

                i += 1
                j += 1

            # Case 2: Current character is a digit
            else:

                # Leading zero is not allowed
                if abbr[j] == '0':
                    return False

                num = 0

                # Read the complete number
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1

                # Skip 'num' characters in word
                i += num

        # Both strings must finish together
        return i == len(word) and j == len(abbr)