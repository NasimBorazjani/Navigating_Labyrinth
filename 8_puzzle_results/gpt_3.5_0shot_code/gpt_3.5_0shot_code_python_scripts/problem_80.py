
from queue import PriorityQueue

def manhattan_distance(state):
    goal_state = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != '_':
                num = state[i][j]
                x_goal, y_goal = divmod(num - 1, 3)
                distance += abs(x_goal - i) + abs(y_goal - j)
    return distance

def get_neighbors(state):
    neighbors = []
    x, y = None, None
    for i in range(3):
        for j in range(3):
            if state[i][j] == '_':
                x, y = i, j
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row.copy() for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def a_star_search(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {tuple(map(tuple, initial_state)): None}
    g_score = {tuple(map(tuple, initial_state)): 0}
    
    while not frontier.empty():
        _, current_state = frontier.get()
        
        if current_state == [[9, 8, 7], [6, 5, 4], [3, 2, 1]]:
            path = []
            while current_state != initial_state:
                path.append(current_state[0][0])
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

initial_state = [[97, 78, '_', 9, 67], [18, 65, 52, 27, 66], [38, 92, 50, 14, 6]]
solution = a_star_search(initial_state)
print(solution)
