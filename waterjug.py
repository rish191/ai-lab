from collections import deque

def water_jug(x, y, target):
    visited = set()
    q = deque([(0, 0)])

    while q:
        a, b = q.popleft()

        if (a, b) in visited:
            continue
        visited.add((a, b))

        print(a, b)

        if a == target or b == target:
            return True

        q.append((x, b))
        q.append((a, y))
        q.append((0, b))
        q.append((a, 0))

        pour = min(a, y - b)
        q.append((a - pour, b + pour))

        pour = min(b, x - a)
        q.append((a + pour, b - pour))

    return False

water_jug(4, 3, 2)