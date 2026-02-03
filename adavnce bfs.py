from collections import deque

grid = [
    [0, 1, 0, 0],
    [0, -1, 0, 1],
    [0, 0, 0, 0],
    [1, 0, -1, 0]
]

start = (0, 0)
goal = (3, 3)

rows, cols = len(grid), len(grid[0])

def advanced_bfs(start, goal):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        x, y = queue.popleft()

        if (x, y) == goal:
            path = []
            while (x, y) is not None:
                path.append((x, y))
                x, y = parent[(x, y)]
            return path[::-1]

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] != -1 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    parent[(nx, ny)] = (x, y)
                    queue.append((nx, ny))
    return []

path = advanced_bfs(start, goal)
print(path)
