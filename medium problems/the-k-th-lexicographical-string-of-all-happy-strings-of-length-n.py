from itertools import product


def getHappyString(n: int, k: int) -> str:
    # if k < 1 or n < 1:
    #     return ""
    #
    # found = 0
    #
    # def backtrack(candidate, last):
    #     if len(candidate) == n:
    #         nonlocal found
    #         found += 1
    #         return candidate if found == k else None
    #
    #     for letter in "abc":
    #         if letter != last:
    #             candidate.append(letter)
    #             ans = backtrack(candidate, letter)
    #             if ans:
    #                 return ans
    #             candidate.pop()
    #     return None
    #
    # ans = backtrack([], None)
    # return "".join(ans) if ans else ""
    # calculate total number of happy strings of length n
    total = 3 * 2 ** (n - 1)
    if k > total:
        return ""

    # alphabet:
    chars = set('abc')
    # last used letter (begin with empty):
    last = ''

    result = [''] * n
    for i in range(n):
        # list of possible letters after the last used one:
        choice = sorted(chars - set(last))
        # how many substrings of length (n-i-1) are possible:
        total //= len(choice)
        # pick the letter at index i:
        last = choice[(k - 1) // total]
        result[i] = last
        # reduce k to pick from substrings:
        k %= total

    return ''.join(result)


getHappyString(3, 2)