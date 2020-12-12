import collections
from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
    # rows = len(grid)
    # cols = len(grid[0])
    # rotten = collections.deque()
    # fresh = 0
    # for r in range(rows):
    #     for c in range(cols):
    #         if grid[r][c] == 2:
    #             rotten.append((r, c))
    #         elif grid[r][c] == 1:
    #             fresh += 1
    #
    # minutes = 0
    #
    # while rotten and fresh > 0:
    #     minutes += 1
    #     for i in range(len(rotten)):
    #         x, y = rotten.popleft()
    #         for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
    #             xx = x + dx
    #             yy = y + dy
    #             if xx < 0 or xx == rows:
    #                 continue
    #             if yy < 0 or yy == cols:
    #                 continue
    #             if grid[xx][yy] == 2 or grid[xx][yy] == 0:
    #                 continue
    #             fresh -= 1
    #             grid[xx][yy] = 2
    #             rotten.append((xx, yy))
    # return minutes if fresh == 0 else -1

    rotten = collections.deque()
    fresh = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                fresh += 1
            elif grid[i][j] == 2:
                rotten.append((i, j))
    minutes = 0
    while rotten and fresh > 0:
        minutes += 1
        x, y = rotten.popleft()
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dx = x + i
            dy = y + j
            if dx == -1 or dx == len(grid):
                continue
            if dy == -1 or dy == len(grid[0]):
                continue
            if grid[dx][dy] == 0 or grid[dx][dy] == 2:
                continue

            fresh -= 1
            grid[dx][dy] = 2
            rotten.append((dx, dy))
    return minutes if fresh == 0 else -1


orangesRotting([[2,1,1],[1,1,0],[0,1,1]])