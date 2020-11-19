class Solution:
    def toLowerCase(self, str: str) -> str:
        alpha = dict(A='a', B='b', C='c', D='d', E='e', F='f', G='g', H='h', I='i', J='j', K='k', L='l', M='m', N='n',
                     O='o', P='p', Q='q', R='r', S='s', T='t', U='u', V='v', W='w', X='x', Y='y', Z='z')
        new_str = ""
        for i in range(len(str)):
            if alpha.get(str[i]) is not None:
                new_str += alpha.get(str[i])
                continue
            new_str += str[i]
        return new_str