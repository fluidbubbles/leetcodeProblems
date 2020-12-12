def equationsPossible(equations):
    graph = [[] for i in range(26)]
    for equation in equations:
        if equation[1] == "=":
            x = ord(equation[0]) - ord("a")
            y = ord(equation[3]) - ord("a")
            graph[x].append(y)
            graph[y].append(x)
    equals = [None] * 26
    t = 0
    for i in range(26):
        if not equals[i]:
            t += 1
            stack = [i]
            while stack:
                node = stack.pop()
                for j in graph[node]:
                    if not equals[j]:
                        equals[j] = t
                        stack.append(j)

    for equation in equations:
        if equation[1] == "!":
            x = ord(equation[0]) - ord("a")
            y = ord(equation[3]) - ord("a")
            if x == y:
                return False
            if equals[x] and equals[x] == equals[y]:
                return False
    return True

equationsPossible(["c==c","f!=a","a==b","a==c"])