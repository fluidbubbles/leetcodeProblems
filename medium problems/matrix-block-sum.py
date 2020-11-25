from typing import List


def matrixBlockSum(mat: List[List[int]], K: int) -> List[List[int]]:
    # ans = []
    # dic = {}
    # for i in range(len(mat)):
    #     r_lower = i - k if i - k > 0 else 0
    #     r_upper = i + k if i + k < len(mat) else len(mat) - 1
    #     arr = []
    #     for j in range(len(mat[i])):
    #         c_lower = j - k if j - k > 0 else 0
    #         c_upper = j + k if j + k < len(mat[i]) else len(mat[i]) - 1
    #         all_sum = 0
    #         for r in range(r_lower, r_upper+1):
    #             for c in range(c_lower, c_upper+1):
    #                 all_sum += mat[r][c]
    #         arr.append(all_sum)
    #     ans.append(arr)
    # return ans
    # m, n = len(mat), len(mat[0])
    # mat[:] = [[0] * (n + 1)] + [[0] + row for row in mat]
    # res = [[0] * n for i in range(m)]
    #
    # for i in range(1, m + 1):
    #     for j in range(1, n + 1):
    #         mat[i][j] += mat[i - 1][j] + mat[i][j - 1] - mat[i - 1][j - 1]
    #
    # for i in range(m):
    #     for j in range(n):
    #         r1, r2 = max(i - K, 0), min(i + K + 1, m)
    #         c1, c2 = max(j - K, 0), min(j + K + 1, n)
    #         res[i][j] = mat[r2][c2] - mat[r2][c1] - mat[r1][c2] + mat[r1][c1]
    #
    # return res
        h, w = len(mat), len(mat[0])
        integral_image = [[0 for y in range(w)] for x in range(h)]

        # building integral image to speed up block sum computation
        for y in range(0, h):
            summation = 0

            for x in range(0, w):
                summation += mat[y][x]
                integral_image[y][x] = summation

                if y > 0:
                    integral_image[y][x] += integral_image[y - 1][x]

        # compute block sum by looking-up integral image
        output_image = [[0 for y in range(w)] for x in range(h)]

        for y in range(h):
            for x in range(w):

                min_row, max_row = max(0, y - K), min(h - 1, y + K)
                min_col, max_col = max(0, x - K), min(w - 1, x + K)

                output_image[y][x] = integral_image[max_row][max_col]

                if min_row > 0:
                    output_image[y][x] -= integral_image[min_row - 1][max_col]

                if min_col > 0:
                    output_image[y][x] -= integral_image[max_row][min_col - 1]

                if min_col > 0 and min_row > 0:
                    output_image[y][x] += integral_image[min_row - 1][min_col - 1]

        return output_image

matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]],1)