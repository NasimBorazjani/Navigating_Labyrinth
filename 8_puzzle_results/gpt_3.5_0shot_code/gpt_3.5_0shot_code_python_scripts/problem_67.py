
from queue import PriorityQueue

def manhattan_distance(state):
    goal_state = [[58, 51, 56, 43, 33], [91, 71, 21, 14, 24], [46, 45, 44, 17, 13]]
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
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = empty_row + dr, empty_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 5:
            new_state = [row.copy() for row in state]
            new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
            neighbors.append(new_state)
    return neighbors

def solve_puzzle(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {tuple(map(tuple, initial_state)): None}
    g_score = {tuple(map(tuple, initial_state)): 0}
    
    while not frontier.empty():
        _, current_state = frontier.get()
        
        if current_state == [[58, 51, 56, 43, 33], [91, 71, 21, 14, 24], [46, 45, 44, 17, 13]]:
            path = []
            while current_state != initial_state:
                path.append(current_state[2][2])
                current_state = came_from[tuple(map(tuple, current_state))]
            return path[::-1]
        
        for neighbor in get_neighbors(current_state):
            new_g_score = g_score[tuple(map(tuple, current_state))] + 1
            if tuple(map(tuple, neighbor)) not in g_score or new_g_score < g_score[tuple(map(tuple, neighbor))]:
                g_score[tuple(map(tuple, neighbor))] = new_g_score
                priority = new_g_score + manhattan_distance(neighbor)
                frontier.put((priority, neighbor))
                came_from[tuple(map(tuple, neighbor))] = current_state
    
    return None

initial_state = [[58, 51, 56, 43, 33], [91, 71, 21, 14, 24], [46, 45, '_', 17, 13]]
solution = solve_puzzle(initial_state)
print(solution)
