from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False for _ in range(n)] for _ in range(m)]

        def checkNeighbours(x, y):
            if x >= 0 and x < m and y >= 0 and y < n and not visited[x][y] and grid[x][y] == "1":
                q.append((x, y))
                visited[x][y] = True

        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    q = deque()
                    q.append((i, j))
                    while len(q) != 0:
                        x, y = q.popleft()
                        visited[x][y] = True
                        checkNeighbours(x - 1, y)
                        checkNeighbours(x + 1, y)
                        checkNeighbours(x, y - 1)
                        checkNeighbours(x, y + 1)

                    islands += 1

        return islands
