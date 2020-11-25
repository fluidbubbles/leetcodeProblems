powers = {1: 0}

def find_power(num):
    power = 1
    if powers.get(num) is not None:
        return powers.get(num)
    else:
        if num & 1:
            power += find_power(num * 3 + 1)
            powers[num] = power
        else:
            power += find_power(num // 2)
            powers[num] = power
    return power


def getKth( lo: int, hi: int, k: int) -> int:
    dic = []
    for i in range(lo, hi + 1):
        dic.append((i, find_power(i)))
    dic.sort(key=lambda tup: tup[1])
    return dic[k-1][0]

print(getKth(1,1000,777))