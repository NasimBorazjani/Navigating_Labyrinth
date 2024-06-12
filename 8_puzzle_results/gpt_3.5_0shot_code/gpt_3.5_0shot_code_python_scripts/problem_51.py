
import heapq

def manhattan_distance(state):
    goal_state = [[96, 53, 19, 15], [37, 32, '_', 87], [78, 100, 17, 13]]
    distance = 0
    for i in range(3):
        for j in range(4):
            if state[i][j] != '_':
                x, y = divmod(goal_state.index(state[i][j]), 4)
                distance += abs(i - x) + abs(j - y)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_row, empty_col = [(i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == '_'][0]
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = empty_row + dr, empty_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 4:
            new_state = [row.copy() for row in state]
            new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
            neighbors.append(new_state)
    return neighbors

def a_star_search(initial_state):
    heap = [(manhattan_distance(initial_state), 0, initial_state, [])]
    visited = set()
    
    while heap:
        _, cost, state, path = heapq.heappop(heap)
        
        if state == [[96, 53, 19, 15], [37, 32, '_', 87], [78, 100, 17, 13]]:
            return path
        
        visited.add(str(state))
        
        for neighbor in get_neighbors(state):
            if str(neighbor) not in visited:
                new_cost = cost + 1
                heapq.heappush(heap, (new_cost + manhattan_distance(neighbor), new_cost, neighbor, path + [neighbor[empty_row][empty_col]]))

initial_state = [[96, 53, 19, 15], [37, 32, '_', 87], [78, 100, 17, 13]]
solution = a_star_search(initial_state)
print(solution)
