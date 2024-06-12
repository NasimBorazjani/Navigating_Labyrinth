
import heapq

def manhattan_distance(state):
    goal_state = [[87, 50, 82], [68, 61, 74], [23, 11, '_']]
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != '_':
                x, y = divmod(state[i][j] - 1, 3)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_row, empty_col = next((i, j) for i in range(3) for j in range(3) if state[i][j] == '_')
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
        
        if state == [[87, 50, 82], [68, 61, 74], [23, 11, '_']]:
            return path
        
        visited.add(str(state))
        
        for neighbor in get_neighbors(state):
            if str(neighbor) not in visited:
                new_cost = cost + 1 + manhattan_distance(neighbor)
                heapq.heappush(heap, (new_cost, cost + 1, neighbor, path + [neighbor[empty_row][empty_col]]))

initial_state = [[87, 50, 82], [68, '_', 74], [23, 61, 11]]
solution = a_star_search(initial_state)
print(solution)
