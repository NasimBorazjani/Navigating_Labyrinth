
from queue import PriorityQueue

def manhattan_distance(state):
    goal_state = [[94, 92, 77, 88, 87], [85, 82, 79, 76, 75], [66, 43, 24, 17, '_']]
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
            neighbor = [row.copy() for row in state]
            neighbor[empty_row][empty_col], neighbor[i][j] = neighbor[i][j], neighbor[empty_row][empty_col]
            neighbors.append(neighbor)
    return neighbors

def solve_puzzle(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {tuple(map(tuple, initial_state)): None}
    g_score = {tuple(map(tuple, initial_state)): 0}
    
    while not frontier.empty():
        _, current_state = frontier.get()
        
        if current_state == [[94, 92, 77, 88, 87], [85, 82, 79, 76, 75], [66, 43, 24, 17, '_']]:
            path = []
            while current_state != initial_state:
                path.append(current_state[2][4])
                current_state = came_from[tuple(map(tuple, current_state))]
            return path[::-1]
        
        for neighbor in get_neighbors(current_state):
            new_g_score = g_score[tuple(map(tuple, current_state))] + 1
            if tuple(map(tuple, neighbor)) not in g_score or new_g_score < g_score[tuple(map(tuple, neighbor))]:
                g_score[tuple(map(tuple, neighbor))] = new_g_score
                f_score = new_g_score + manhattan_distance(neighbor)
                frontier.put((f_score, neighbor))
                came_from[tuple(map(tuple, neighbor))] = current_state
    
    return None

initial_state = [[94, 92, 77, 88, '_'], [82, 43, 76, 85, 87], [24, 66, 17, 79, 75]]
solution = solve_puzzle(initial_state)
print(solution)
