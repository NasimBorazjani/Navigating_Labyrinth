
import heapq

def manhattan_distance(state):
    goal_state = [[34, 68, 46, 20], [12, 18, '_', 5], [53, 7, 65, 47]]
    distance = 0
    for i in range(3):
        for j in range(4):
            if state[i][j] != '_':
                x, y = divmod(state[i][j] - 1, 4)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_row, empty_col = None, None
    for i in range(3):
        for j in range(4):
            if state[i][j] == '_':
                empty_row, empty_col = i, j
                break
    for i, j in [(empty_row-1, empty_col), (empty_row+1, empty_col), (empty_row, empty_col-1), (empty_row, empty_col+1)]:
        if 0 <= i < 3 and 0 <= j < 4:
            new_state = [row.copy() for row in state]
            new_state[empty_row][empty_col], new_state[i][j] = new_state[i][j], new_state[empty_row][empty_col]
            neighbors.append(new_state)
    return neighbors

def a_star_search(initial_state):
    heap = [(manhattan_distance(initial_state), 0, initial_state, [])]
    visited = set()
    
    while heap:
        _, cost, state, path = heapq.heappop(heap)
        
        if state == [[34, 68, 46, 20], [12, 18, '_', 5], [53, 7, 65, 47]]:
            return path
        
        visited.add(str(state))
        
        for neighbor in get_neighbors(state):
            if str(neighbor) not in visited:
                new_cost = cost + 1
                new_path = path + [neighbor[empty_row][empty_col]]
                heapq.heappush(heap, (new_cost + manhattan_distance(neighbor), new_cost, neighbor, new_path))

initial_state = [[34, 68, 46, 20], [12, 18, '_', 5], [53, 7, 65, 47]]
solution = a_star_search(initial_state)
print(solution)
