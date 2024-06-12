
import heapq

def manhattan_distance(state):
    goal_state = [[78, 98, 89], [38, 28, 7], [58, 95, 70]]
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != '_':
                x, y = divmod(state[i][j] - 1, 3)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_row, empty_col = next((i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == '_')
    for i, j in [(empty_row-1, empty_col), (empty_row+1, empty_col), (empty_row, empty_col-1), (empty_row, empty_col+1)]:
        if 0 <= i < 3 and 0 <= j < 3:
            new_state = [row.copy() for row in state]
            new_state[empty_row][empty_col], new_state[i][j] = new_state[i][j], new_state[empty_row][empty_col]
            neighbors.append(new_state)
    return neighbors

def a_star_search(initial_state):
    heap = [(manhattan_distance(initial_state), 0, initial_state, [])]
    visited = set()
    
    while heap:
        _, cost, state, path = heapq.heappop(heap)
        
        if state == [[78, 98, 89], [38, 28, 7], [58, 95, 70]]:
            return path
        
        if tuple(map(tuple, state)) in visited:
            continue
        
        visited.add(tuple(map(tuple, state)))
        
        for neighbor in get_neighbors(state):
            heapq.heappush(heap, (cost + 1 + manhattan_distance(neighbor), cost + 1, neighbor, path + [neighbor[empty_row][empty_col]]))
    
    return None

initial_state = [[78, 98, 89], [38, 28, 7], [58, 95, 70]]
solution = a_star_search(initial_state)
print(solution)
