
import heapq

def manhattan_distance(state):
    goal_state = [[74, 37, 2, 22], [4, 21, '_', 54], [33, 70, 9, 11]]
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
        
        if state == [[74, 37, 2, 22], [4, 21, '_', 54], [33, 70, 9, 11]]:
            return path
        
        if tuple(map(tuple, state)) in visited:
            continue
        
        visited.add(tuple(map(tuple, state)))
        
        for neighbor in get_neighbors(state):
            heapq.heappush(heap, (manhattan_distance(neighbor) + cost + 1, cost + 1, neighbor, path + [neighbor[empty_row][empty_col]]))

initial_state = [[74, 37, 2, 22], [4, 21, '_', 54], [33, 70, 9, 11]]
solution = a_star_search(initial_state)
print(solution)
