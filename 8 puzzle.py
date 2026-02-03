import heapq

goal_state = ((1,2,3),
              (4,5,6),
              (7,8,0))  # 0 represents the blank tile

moves = {'Up': (-1,0), 'Down': (1,0), 'Left': (0,-1), 'Right': (0,1)}

def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x, goal_y = divmod(val-1, 3)
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

def get_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def swap(state, x1, y1, x2, y2):
    lst = [list(row) for row in state]
    lst[x1][y1], lst[x2][y2] = lst[x2][y2], lst[x1][y1]
    return tuple(tuple(row) for row in lst)

def get_neighbors(state):
    neighbors = []
    x, y = get_blank(state)
    for move, (dx, dy) in moves.items():
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = swap(state, x, y, nx, ny)
            neighbors.append((move, new_state))
    return neighbors

def a_star(start):
    pq = []
    heapq.heappush(pq, (manhattan(start), 0, start, []))
    visited = set()
    
    while pq:
        f, g, state, path = heapq.heappop(pq)
        if state == goal_state:
            return path
        if state in visited:
            continue
        visited.add(state)
        
        for move, neighbor in get_neighbors(state):
            if neighbor not in visited:
                heapq.heappush(pq, (g+1+manhattan(neighbor), g+1, neighbor, path + [move]))
    return None

# Example starting state
start_state = ((2,8,3),
               (1,6,4),
               (7,0,5))

solution = a_star(start_state)
print("Solution moves:", solution)
print("Number of moves:", len(solution))
