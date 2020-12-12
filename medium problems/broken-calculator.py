def brokenCalc(x: int, y: int) -> int:
    if x > y:
        return x - y
    steps = 0
    while y > x:
        steps += 1
        if y % 2 == 1:
            y += 1
        else:
            y //= 2
    return steps + x - y

brokenCalc(8,10)