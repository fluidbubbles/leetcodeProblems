from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        alpha = "abcdefghijklmnopqrstuvwxyz"
        mapping = {}
        for i in range(len(alpha)):
            mapping[alpha[i]] = code[i]
        seen = {}
        for word in words:
            code = ""
            for char in word:
                code += mapping.get(char)
            seen[code] = "yes"
        return len(seen)
