
from collections import deque

# Map of the trampoline park
map_data = """1 1 0 0 1 1 0 0 1 0 0 1 0 1 0
1 0 1 1 1 1 1 1 1 1 1 1 1 1 0
0 0 0 1 1 0 1 1 1 1 1 1 0 1 1
0 1 1 1 0 1 0 0 1 0 0 1 1 0 1
0 0 1 1 0 0 1 1 0 0 1 0 1 1 1
0 1 0 1 1 0 1 1 0 0 0 0 1 0 0
0 0 1 0 1 1 1 0 1 1 0 1 1 0 0
0 0 0 1 1 0 1 1 0 0 1 1 1 0 0
0 0 1 1 1 0 0 1 1 1 1 0 1 1 0
0 0 0 1 1 1 1 0 0 1 1 1 0 1 1
0 0 0 1 0 1 0 0 1 1 0 1 0 1 0
1 1 0 0 0 1 1 1 1 0 1 1 0 1 0
1 1 1 0 0 0 1 0 0 1 1 1 1 0 1
0 1 1 1 1 0 0 0 1 1 0 1 1 0 1
1 0 0 0 0 1 0 0 0 0 0 1 0 1 0"""

# Convert the map into a 2D list
map_data = [list(map(int, line.split())) for line in map_data.split('\n') if line]

# Function to check if a move is valid
def is_valid(pos, prev_pos, diag_jumps):
    x, y = pos
    if x < 0 or y < 0 or x >= len(map_data) or y >= len(map_data[0]):
        return False
    if map_data[x][y] == 1:
        return False
    if prev_pos is not None:
        dx, dy = pos[0] - prev_pos[0], pos[1] - prev_pos[1]
        if abs(dx) == abs(dy) and (dx + dy) != 5:
            return False
    return True

# Function to find the shortest path
def find_shortest_path(start, end):
    queue = deque([(start, None)])
    visited = set()
    while queue:
        pos, prev_pos = queue.popleft()
        if pos == end:
            path = [pos]
            while prev_pos is not None:
                path.append(prev_pos)
                prev_pos = visited[prev_pos]
            return path[::-1]
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            next_pos = (pos[0] + dx, pos[1] + dy)
            if is_valid(next_pos, pos, 5):
                queue.append((next_pos, pos))
                visited[next_pos] = pos
    return None

# Test the function
start = (14, 10)
end = (2, 1)
shortest_path = find_shortest_path(start, end)
print(shortest_path)
