
import heapq

def manhattan_distance(state):
    goal_state = [[54, 100, 91, 80, 56], [19, 18, 38, 74, 29], [14, 36, 44, 13, 10]]
    distance = 0
    for i in range(3):
        for j in range(5):
            if state[i][j] != '_':
                x, y = divmod(state[i][j] - 1, 5)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_pos = [(i, j) for i in range(3) for j in range(5) if state[i][j] == '_'][0]
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x, y = empty_pos[0] + dx, empty_pos[1] + dy
        if 0 <= x < 3 and 0 <= y < 5:
            new_state = [row.copy() for row in state]
            new_state[empty_pos[0]][empty_pos[1]], new_state[x][y] = new_state[x][y], new_state[empty_pos[0]][empty_pos[1]]
            neighbors.append(new_state)
    return neighbors

def a_star_search(initial_state):
    heap = [(manhattan_distance(initial_state), 0, initial_state, [])]
    visited = set()
    
    while heap:
        _, cost, state, path = heapq.heappop(heap)
        
        if state == [[54, 100, 91, 80, 56], [19, 18, 38, 74, 29], [14, 36, 44, 13, 10]]:
            return path
        
        if tuple(map(tuple, state)) in visited:
            continue
        
        visited.add(tuple(map(tuple, state)))
        
        for neighbor in get_neighbors(state):
            heapq.heappush(heap, (cost + 1 + manhattan_distance(neighbor), cost + 1, neighbor, path + [neighbor[empty_pos[0]][empty_pos[1]]]))

initial_state = [[54, 100, 91, 80, 56], [19, '_', 38, 74, 29], [14, 36, 44, 13, 10]]
solution = a_star_search(initial_state)
print(solution)
