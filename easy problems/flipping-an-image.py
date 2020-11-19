class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            k = 0
            m = len(A[i]) - 1
            while k <= m:
                if k != m:
                    A[i][k] = 1 if A[i][k] == 0 else 0
                    A[i][m] = 1 if A[i][m] == 0 else 0
                    A[i][k], A[i][m] = A[i][m], A[i][k]
                else:
                    A[i][k] = 1 if A[i][k] == 0 else 0
                k += 1
                m -= 1
        return A

