def minFlips(target: str) -> int:
    flips = 0
    for i in range(len(target)):
        if i == 0 and target[0] != "0" or i != 0 and target[i] != target[i - 1]:
            flips += 1
    return flips

minFlips("101")