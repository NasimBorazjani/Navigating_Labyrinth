
from queue import PriorityQueue

initial_state = [[31, 92, 67, 69], [87, 35, 42, 72], [53, '_', 28, 19]]
goal_state = [[92, 87, 72, 69], [67, 53, 42, 35], [31, 28, 19, '_']]

def manhattan_distance(tile1, tile2):
    x1, y1 = tile1
    x2, y2 = tile2
    return abs(x1 - x2) + abs(y1 - y2)

def possible_moves(state):
    moves = []
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == '_':
                if i > 0:
                    moves.append((i-1, j))
                if i < len(state)-1:
                    moves.append((i+1, j))
                if j > 0:
                    moves.append((i, j-1))
                if j < len(state[0])-1:
                    moves.append((i, j+1))
    return moves

def a_star_search(initial_state, goal_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {}
    cost_so_far = {}
    came_from[str(initial_state)] = None
    cost_so_far[str(initial_state)] = 0

    while not frontier.empty():
        current_cost, current_state = frontier.get()

        if current_state == goal_state:
            break

        for next_move in possible_moves(current_state):
            new_cost = current_cost + 1
            if str(next_move) not in cost_so_far or new_cost < cost_so_far[str(next_move)]:
                cost_so_far[str(next_move)] = new_cost
                priority = new_cost + manhattan_distance(next_move, goal_state)
                frontier.put((priority, next_move))
                came_from[str(next_move)] = current_state

    path = []
    current_state = goal_state
    while current_state != initial_state:
        previous_state = came_from[str(current_state)]
        for i in range(len(current_state)):
            for j in range(len(current_state[0]):
                if current_state[i][j] == '_':
                    path.append(previous_state[i][j])
                    break
        current_state = previous_state

    return path[::-1]

solution = a_star_search(initial_state, goal_state)
print(solution)
