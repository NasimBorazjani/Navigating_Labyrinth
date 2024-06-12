
from queue import PriorityQueue

def manhattan_distance(state):
    goal_state = [[98, 30, 85, 44, 59, 40], [56, 68, 50, 61, 47, 15], [37, 48, 24, 81, 22, '_']]
    distance = 0
    for i in range(3):
        for j in range(6):
            if state[i][j] != '_':
                x, y = divmod(goal_state[i].index(state[i][j]), 6)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_row, empty_col = [(i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == '_'][0]
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = empty_row + dr, empty_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 6:
            new_state = [row.copy() for row in state]
            new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
            neighbors.append(new_state)
    return neighbors

def a_star_search(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {tuple(map(tuple, initial_state)): None}
    g_score = {tuple(map(tuple, initial_state)): 0}
    
    while not frontier.empty():
        _, current_state = frontier.get()
        
        if current_state == [[98, 30, 85, 44, 59, 40], [56, 68, 50, 61, 47, 15], [37, 48, 24, 81, 22, '_']]:
            path = []
            while current_state != initial_state:
                path.append(int(current_state[empty_row][empty_col]))
                current_state = came_from[tuple(map(tuple, current_state))]
            return path[::-1]
        
        for neighbor in get_neighbors(current_state):
            new_g_score = g_score[tuple(map(tuple, current_state))] + 1
            if tuple(map(tuple, neighbor)) not in g_score or new_g_score < g_score[tuple(map(tuple, neighbor)]:
                g_score[tuple(map(tuple, neighbor))] = new_g_score
                f_score = new_g_score + manhattan_distance(neighbor)
                frontier.put((f_score, neighbor))
                came_from[tuple(map(tuple, neighbor))] = current_state
    
    return None

initial_state = [[98, 30, 85, 44, 59, 40], [56, 68, 50, 61, 47, 15], [37, 48, 24, 81, 22, '_']]
solution = a_star_search(initial_state)
print(solution)
