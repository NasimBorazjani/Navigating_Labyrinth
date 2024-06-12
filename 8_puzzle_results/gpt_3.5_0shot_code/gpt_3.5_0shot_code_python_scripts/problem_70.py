
import heapq

def manhattan_distance(state):
    goal_state = [[86, 100, 92, 37, 95], [88, '_', 97, 10, 67], [32, 82, 19, 53, 4]]
    distance = 0
    for i in range(3):
        for j in range(5):
            if state[i][j] != '_':
                x, y = divmod(goal_state[i][j], 5)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_row, empty_col = [(i, j) for i in range(3) for j in range(5) if state[i][j] == '_'][0]
    for i, j in [(empty_row-1, empty_col), (empty_row+1, empty_col), (empty_row, empty_col-1), (empty_row, empty_col+1)]:
        if 0 <= i < 3 and 0 <= j < 5:
            new_state = [row.copy() for row in state]
            new_state[empty_row][empty_col], new_state[i][j] = new_state[i][j], new_state[empty_row][empty_col]
            neighbors.append(new_state)
    return neighbors

def a_star_search(initial_state):
    heap = [(manhattan_distance(initial_state), 0, initial_state)]
    visited = set()
    
    while heap:
        _, cost, state = heapq.heappop(heap)
        
        if state == [[86, 100, 92, 37, 95], [88, '_', 97, 10, 67], [32, 82, 19, 53, 4]]:
            return [tile for tile in path]
        
        visited.add(str(state))
        
        for neighbor in get_neighbors(state):
            if str(neighbor) not in visited:
                heapq.heappush(heap, (cost + 1 + manhattan_distance(neighbor), cost + 1, neighbor))
    
    return None

initial_state = [[86, 100, 92, 37, 95], [88, '_', 97, 10, 67], [32, 82, 19, 53, 4]]
path = a_star_search(initial_state)
print(path)
