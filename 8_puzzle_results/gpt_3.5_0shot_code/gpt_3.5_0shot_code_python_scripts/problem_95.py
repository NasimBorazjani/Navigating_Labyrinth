
from queue import PriorityQueue

def manhattan_distance(state):
    goal_state = [[92, 72, 91, 79, 62, 24], [93, 67, 65, 63, 83, 74], [41, 34, 29, 27, 58, '_']]
    distance = 0
    for i in range(3):
        for j in range(6):
            if state[i][j] != '_':
                x_goal, y_goal = divmod(goal_state[i].index(state[i][j]), 6)
                distance += abs(i - x_goal) + abs(j - y_goal)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_pos = [(i, j) for i in range(3) for j in range(6) if state[i][j] == '_'][0]
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x, y = empty_pos[0] + dx, empty_pos[1] + dy
        if 0 <= x < 3 and 0 <= y < 6:
            new_state = [row.copy() for row in state]
            new_state[empty_pos[0]][empty_pos[1]], new_state[x][y] = new_state[x][y], new_state[empty_pos[0]][empty_pos[1]]
            neighbors.append(new_state)
    return neighbors

def a_star_search(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {tuple(map(tuple, initial_state)): None}
    g_score = {tuple(map(tuple, initial_state)): 0}
    
    while not frontier.empty():
        _, current_state = frontier.get()
        
        if current_state == [[92, 72, 91, 79, 62, 24], [93, 67, 65, 63, 83, 74], [41, 34, 29, 27, 58, '_']]:
            path = []
            while current_state != initial_state:
                path.append(int(current_state[empty_pos[0]][empty_pos[1]]))
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

initial_state = [[92, 72, 91, 79, 62, 24], [93, 67, 65, 63, 83, 74], [41, 34, 29, 27, 58, '_']]
solution = a_star_search(initial_state)
print(solution)
