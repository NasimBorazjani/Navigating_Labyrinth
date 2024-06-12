
from queue import PriorityQueue

def manhattan_distance(state):
    goal_state = [[94, 91, 76, 74, 29, 1], [61, 93, 17, 37, 34, 2], [67, 32, 55, 19, 26, 3]]
    distance = 0
    for i in range(3):
        for j in range(6):
            if state[i][j] != '_':
                x_goal, y_goal = divmod(goal_state[i].index(state[i][j]), 6)
                x_state, y_state = divmod(j, 6)
                distance += abs(x_goal - x_state) + abs(y_goal - y_state)
    return distance

def get_neighbors(state):
    neighbors = []
    x, y = [(i, j) for i in range(3) for j in range(6) if state[i][j] == '_'][0]
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 6:
            new_state = [row.copy() for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append((new_state, (new_x, new_y)))
    return neighbors

def a_star_search(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state, []))
    visited = set()
    
    while not frontier.empty():
        _, current_state, path = frontier.get()
        
        if current_state == [[94, 91, 76, 74, 29, 1], [61, 93, 17, 37, 34, 2], [67, 32, 55, 19, 26, 3]]:
            return path
        
        visited.add(str(current_state))
        
        for neighbor, move in get_neighbors(current_state):
            if str(neighbor) not in visited:
                new_path = path + [neighbor[move[0]][move[1]]]
                frontier.put((len(new_path) + manhattan_distance(neighbor), neighbor, new_path))

initial_state = [[94, 91, 76, '_', 74, 29], [61, 93, 17, 37, 34, 44], [67, 32, 55, 19, 26, 69]]
solution = a_star_search(initial_state)
print(solution)
