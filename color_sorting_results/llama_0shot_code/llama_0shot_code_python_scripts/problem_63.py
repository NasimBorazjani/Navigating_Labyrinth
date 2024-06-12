
from collections import deque

def get_moves(state):
    moves = []
    for from_tube in range(len(state)):
        if state[from_tube]:  # if the tube is not empty
            for to_tube in range(len(state)):
                if from_tube != to_tube and len(state[to_tube]) < 8:  # if the move is allowed
                    moves.append((from_tube, to_tube))
    return moves

def dfs(state, path):
    if not state:  # if the state is the goal state
        return path
    for move in get_moves(state):
        new_state = deque(state)
        ball = new_state[move[0]].pop()  # take a ball from the 'from_tube'
        new_state[move[1]].append(ball)  # put the ball into the 'to_tube'
        result = dfs(tuple(new_state), path + [move])  # recursive call with the new state and the current path plus the move
        if result is not None:
            return result  # if the new state is the goal state, return the current path plus the move that led to it
    return None

# initial state
initial_state = (['Blue', 'Green', 'Blue', 'Red', 'Green'],
                 ['Blue', 'Green', 'Green', 'Red', 'Blue'],
                 ['Red', 'Blue', 'Red', 'Red', 'Green'])

# convert the initial state to a more convenient data structure: a list of deques, where each deque represents a tube
initial_state = [deque(colors[::-1]) for colors in initial_state]

# find the shortest list of move tuples that will result in all the balls being correctly sorted
shortest_path = dfs(tuple(initial_state), [])

print(shortest_path)
