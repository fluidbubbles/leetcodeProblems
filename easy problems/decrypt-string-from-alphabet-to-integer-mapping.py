class Solution:
    def freqAlphabets(self, s: str) -> str:
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
        i = 0
        output = ""
        while i < len(s):
            if len(s) - i > 2 and s[i + 2] == "#":
                num = s[i] + s[i + 1]
                output += alpha[int(num) - 1]
                i += 3
            else:
                output += alpha[int(s[i]) - 1]
                i += 1
        return output
