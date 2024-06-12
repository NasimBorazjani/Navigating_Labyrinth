
from queue import PriorityQueue

def manhattan_distance(state):
    goal_state = [[92, 79, 74, 46, 64, 44], [39, 59, 75, 26, 47, 73], [29, 53, 56, '_', 16, 17]]
    distance = 0
    for i in range(3):
        for j in range(6):
            if state[i][j] != '_':
                x, y = divmod(state[i][j] - 1, 6)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_i, empty_j = None, None
    for i in range(3):
        for j in range(6):
            if state[i][j] == '_':
                empty_i, empty_j = i, j
                break
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_i, new_j = empty_i + di, empty_j + dj
        if 0 <= new_i < 3 and 0 <= new_j < 6:
            new_state = [row.copy() for row in state]
            new_state[empty_i][empty_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_i][empty_j]
            neighbors.append(new_state)
    return neighbors

def solve_puzzle(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {tuple(map(tuple, initial_state)): None}
    g_score = {tuple(map(tuple, initial_state)): 0}
    
    while not frontier.empty():
        _, current_state = frontier.get()
        if current_state == [[92, 79, 74, 46, 64, 44], [39, 59, 75, 26, 47, 73], [29, 53, 56, '_', 16, 17]]:
            path = []
            while current_state != initial_state:
                path.append(current_state[2][5])
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

initial_state = [[92, 79, 74, 46, 64, 44], [39, 59, 75, 26, 47, 73], [29, 53, 56, '_', 16, 17]]
solution = solve_puzzle(initial_state)
print(solution)
