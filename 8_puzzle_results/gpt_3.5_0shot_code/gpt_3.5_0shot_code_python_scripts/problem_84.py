
import heapq

def manhattan_distance(state):
    goal_state = [[85, 96, 29, 80, 12], [60, '_', 76, 42, 82], [27, 89, 72, 37, 55]]
    distance = 0
    for i in range(3):
        for j in range(5):
            if state[i][j] != '_':
                x, y = divmod(goal_state[i].index(state[i][j]), 5)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_row, empty_col = [(i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == '_'][0]
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
        
        if state == [[85, 96, 29, 80, 12], [60, '_', 76, 42, 82], [27, 89, 72, 37, 55]]:
            return [val for row in visited for val in row]
        
        visited.add(tuple(row for row in state))
        
        for neighbor in get_neighbors(state):
            if tuple(row for row in neighbor) not in visited:
                heapq.heappush(heap, (cost + 1 + manhattan_distance(neighbor), cost + 1, neighbor))

initial_state = [[85, 96, 29, 80, 12], [60, '_', 76, 42, 82], [27, 89, 72, 37, 55]]
solution = a_star_search(initial_state)
print(solution)
