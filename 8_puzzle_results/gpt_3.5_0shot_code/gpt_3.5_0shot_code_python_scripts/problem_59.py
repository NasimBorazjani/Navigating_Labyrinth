
import heapq

def manhattan_distance(state):
    goal_state = [[10, 96, 60, '_'], [98, 73, 14, 58], [53, 3, 21, 67]]
    distance = 0
    for i in range(3):
        for j in range(4):
            if state[i][j] != '_':
                x, y = divmod(goal_state.index(state[i][j]), 4)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_row, empty_col = [(i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == '_'][0]
    for i, j in [(empty_row-1, empty_col), (empty_row+1, empty_col), (empty_row, empty_col-1), (empty_row, empty_col+1)]:
        if 0 <= i < 3 and 0 <= j < 4:
            new_state = [row.copy() for row in state]
            new_state[empty_row][empty_col], new_state[i][j] = new_state[i][j], new_state[empty_row][empty_col]
            neighbors.append(new_state)
    return neighbors

def a_star_search(initial_state):
    frontier = [(manhattan_distance(initial_state), 0, initial_state)]
    heapq.heapify(frontier)
    visited = set()
    
    while frontier:
        _, cost, state = heapq.heappop(frontier)
        if state == [[10, 96, 60, '_'], [98, 73, 14, 58], [53, 3, 21, 67]]:
            return cost
        visited.add(str(state))
        
        for neighbor in get_neighbors(state):
            if str(neighbor) not in visited:
                heapq.heappush(frontier, (manhattan_distance(neighbor) + cost + 1, cost + 1, neighbor))

initial_state = [[10, 96, 60, '_'], [98, 73, 14, 58], [53, 3, 21, 67]]
shortest_path_length = a_star_search(initial_state)
print(shortest_path_length)
