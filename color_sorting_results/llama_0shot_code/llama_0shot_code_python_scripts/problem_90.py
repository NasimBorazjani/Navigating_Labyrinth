
from collections import deque

def get_moves(state):
    moves = []
    for i in range(len(state)):
        if state[i]:  # if the tube is not empty
            color = state[i][-1]
            for j in range(len(state)):
                if j != i and state[j] and state[j][-1] == color and len(state[j]) < 9:
                    moves.append((i, j))
    return moves

def make_move(state, move):
    i, j = move
    color = state[i].pop()
    state[j].append(color)
    return state

def is_goal(state):
    for tube in state:
        if len(set(tube)) != 1:
            return False
    return True

def solve(state):
    queue = deque([([], state)])
    while queue:
        path, state = queue.popleft()
        if is_goal(state):
            return path
        for move in get_moves(state):
            new_state = make_move(list(state), move)
            queue.append((path + [move], new_state))

initial_state = [['Green', 'Green', 'Red', 'Green', 'Red', 'Red'], 
                 ['Green', 'Red', 'Blue', 'Blue', 'Red', 'Blue'], 
                 ['Blue', 'Green', 'Blue', 'Blue', 'Red', 'Green']]

print(solve(initial_state))
