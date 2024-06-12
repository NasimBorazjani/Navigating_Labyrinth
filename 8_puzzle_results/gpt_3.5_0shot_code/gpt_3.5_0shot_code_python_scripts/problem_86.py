
import heapq

def manhattan_distance(state):
    goal_state = [[88, 71, 83, 72, 37], [98, 43, 53, 54, 82], [24, 20, 21, 14, '_']]
    distance = 0
    for i in range(3):
        for j in range(5):
            if state[i][j] != '_':
                x, y = divmod(state[i][j] - 1, 5)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_row, empty_col = None, None
    for i in range(3):
        for j in range(5):
            if state[i][j] == '_':
                empty_row, empty_col = i, j
                break
    for i, j in [(empty_row-1, empty_col), (empty_row+1, empty_col), (empty_row, empty_col-1), (empty_row, empty_col+1)]:
        if 0 <= i < 3 and 0 <= j < 5:
            new_state = [row.copy() for row in state]
            new_state[empty_row][empty_col], new_state[i][j] = new_state[i][j], '_'
            neighbors.append(new_state)
    return neighbors

def a_star_search(initial_state):
    heap = [(manhattan_distance(initial_state), 0, initial_state, [])]
    visited = set()
    
    while heap:
        _, cost, state, path = heapq.heappop(heap)
        
        if state == [[88, 71, 83, 72, 37], [98, 43, 53, 54, 82], [24, 20, 21, 14, '_']]:
            return path
        
        visited.add(str(state))
        
        for neighbor in get_neighbors(state):
            if str(neighbor) not in visited:
                new_cost = cost + 1
                heapq.heappush(heap, (new_cost + manhattan_distance(neighbor), new_cost, neighbor, path + [neighbor[empty_row][empty_col]]))

initial_state = [[88, 71, 83, 72, 37], [98, 43, 53, '_', 82], [24, 20, 54, 14, 21]]
solution = a_star_search(initial_state)
print(solution)
