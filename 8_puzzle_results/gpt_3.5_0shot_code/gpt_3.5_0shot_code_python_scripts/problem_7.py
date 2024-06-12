
import heapq

def manhattan_distance(state):
    goal_state = [[36, 16, 48], [86, '_', 13], [89, 31, 37]]
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != '_':
                x, y = divmod(goal_state.index(state[i][j]), 3)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_row, empty_col = next((i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == '_')
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = empty_row + dr, empty_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [row.copy() for row in state]
            new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], '_'
            neighbors.append(new_state)
    return neighbors

def a_star_search(initial_state):
    heap = [(manhattan_distance(initial_state), 0, initial_state, [])]
    visited = set()
    
    while heap:
        _, cost, state, path = heapq.heappop(heap)
        
        if state == [[36, 16, 48], [86, '_', 13], [89, 31, 37]]:
            return path
        
        if tuple(map(tuple, state)) in visited:
            continue
        
        visited.add(tuple(map(tuple, state)))
        
        for neighbor in get_neighbors(state):
            heapq.heappush(heap, (manhattan_distance(neighbor) + cost + 1, cost + 1, neighbor, path + [neighbor[empty_row][empty_col]]))

initial_state = [[36, 16, 48], [86, '_', 13], [89, 31, 37]]
solution = a_star_search(initial_state)
print(solution)
