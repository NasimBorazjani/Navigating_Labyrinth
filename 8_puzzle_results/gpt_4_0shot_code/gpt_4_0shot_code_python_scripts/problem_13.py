
from queue import PriorityQueue

def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def get_position(state, element):
    for row in range(len(state)):
        if element in state[row]:
            return (row, state[row].index(element))

def get_moves(state):
    moves = []
    pos = get_position(state, '_')
    if pos[0] > 0:
        moves.append('up')
    if pos[0] < 2:
        moves.append('down')
    if pos[1] > 0:
        moves.append('left')
    if pos[1] < 2:
        moves.append('right')
    return moves

def swap(state, pos1, pos2):
    new_state = [row[:] for row in state]
    new_state[pos1[0]][pos1[1]], new_state[pos2[0]][pos2[1]] = new_state[pos2[0]][pos2[1]], new_state[pos1[0]][pos1[1]]
    return new_state

def solve(initial_state):
    goal_state = [[97, 82, 61], [51, 43, 41], [36, 29, '_']]
    queue = PriorityQueue()
    queue.put((0, initial_state))
    came_from = {str(initial_state): None}
    cost_so_far = {str(initial_state): 0}
    while not queue.empty():
        _, current = queue.get()
        if current == goal_state:
            break
        for move in get_moves(current):
            pos = get_position(current, '_')
            if move == 'up':
                new_state = swap(current, pos, (pos[0] - 1, pos[1]))
            elif move == 'down':
                new_state = swap(current, pos, (pos[0] + 1, pos[1]))
            elif move == 'left':
                new_state = swap(current, pos, (pos[0], pos[1] - 1))
            else:
                new_state = swap(current, pos, (pos[0], pos[1] + 1))
            new_cost = cost_so_far[str(current)] + 1
            if str(new_state) not in cost_so_far or new_cost < cost_so_far[str(new_state)]:
                cost_so_far[str(new_state)] = new_cost
                priority = new_cost + heuristic(get_position(new_state, '_'), get_position(goal_state, '_'))
                queue.put((priority, new_state))
                came_from[str(new_state)] = current
    current = goal_state
    path = []
    while current != initial_state:
        prev = came_from[str(current)]
        path.append(prev[get_position(prev, '_')[0]][get_position(prev, '_')[1]])
        current = prev
    path.reverse()
    return path

initial_state = [[41, 36, 82], [29, 97, 43], ['_', 51, 61]]
print(solve(initial_state))
