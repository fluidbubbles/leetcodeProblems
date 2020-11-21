import collections


def sortString(s: str) -> str:
    seen = collections.Counter(s)
    length = len(s)
    s = sorted(set(s))
    length_s = len(s)
    i = 0
    j = len(s) - 1
    output = ""
    while i < length:
        for j in range(length_s):
            if seen[s[j]]:
                seen[s[j]] -= 1
                output += s[j]
                i += 1
        for k in range(length_s - 1, -1, -1):
            if seen[s[k]]:
                seen[s[k]] -= 1
                output += s[k]
                i += 1
    return output


sortString("aaaabbbbcccc")

