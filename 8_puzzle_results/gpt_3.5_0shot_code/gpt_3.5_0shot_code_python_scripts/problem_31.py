
from queue import PriorityQueue

initial_state = [[75, 53, 73, 62], ['_', 14, 90, 43], [21, 17, 51, 27]]
goal_state = [[75, 53, 73, 62], [43, 27, 21, 17], [14, 90, '_', 51]]

def manhattan_distance(state1, state2):
    distance = 0
    for i in range(3):
        for j in range(4):
            if state1[i][j] != '_':
                x1, y1 = divmod(state1[i][j], 4)
                x2, y2 = divmod(state2[i][j], 4)
                distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def possible_moves(state):
    moves = []
    x, y = next((i, j) for i in range(3) for j in range(4) if state[i][j] == '_')
    if x > 0:
        new_state = [row[:] for row in state]
        new_state[x][y], new_state[x - 1][y] = new_state[x - 1][y], new_state[x][y]
        moves.append((new_state, state[x - 1][y]))
    if x < 2:
        new_state = [row[:] for row in state]
        new_state[x][y], new_state[x + 1][y] = new_state[x + 1][y], new_state[x][y]
        moves.append((new_state, state[x + 1][y]))
    if y > 0:
        new_state = [row[:] for row in state]
        new_state[x][y], new_state[x][y - 1] = new_state[x][y - 1], new_state[x][y]
        moves.append((new_state, state[x][y - 1]))
    if y < 3:
        new_state = [row[:] for row in state]
        new_state[x][y], new_state[x][y + 1] = new_state[x][y + 1], new_state[x][y]
        moves.append((new_state, state[x][y + 1]))
    return moves

def a_star_search(initial_state, goal_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state, []))
    explored = set()

    while not frontier.empty():
        cost, current_state, path = frontier.get()

        if current_state == goal_state:
            return path

        if str(current_state) in explored:
            continue

        explored.add(str(current_state))

        for new_state, move in possible_moves(current_state):
            new_cost = len(path) + 1 + manhattan_distance(new_state, goal_state)
            frontier.put((new_cost, new_state, path + [move]))

    return None

solution = a_star_search(initial_state, goal_state)
print(solution)
