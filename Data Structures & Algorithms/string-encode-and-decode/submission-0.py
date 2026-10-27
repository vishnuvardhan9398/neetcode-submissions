from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            encoded += str(len(word)) + "#" + word

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):

            # Find the separator
            j = i

            while s[j] != "#":
                j += 1

            # Get the length of the word
            length = int(s[i:j])

            # Get the actual word
            word = s[j + 1:j + 1 + length]

            result.append(word)

            # Move to the next encoded word
            i = j + 1 + length

        return result