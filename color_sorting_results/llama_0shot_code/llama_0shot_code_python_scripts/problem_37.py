
from collections import deque

def get_moves(state):
    moves = []
    for i in range(len(state)):
        if state[i]:  # if the tube is not empty
            for j in range(len(state)):
                if j != i and len(state[j]) < 7:  # we can move to the tube and it's not full
                    moves.append((i, j))
    return moves

def dfs(state, path):
    if not state:  # if all tubes are sorted
        return path
    min_path = None
    for move in get_moves(state):
        new_state = list(state)
        ball = new_state[move[0]].pop()  # move the ball from the 'from' tube
        new_state[move[1]].append(ball)  # to the 'to' tube
        new_path = list(path)
        new_path.append(move)
        result = dfs(tuple(new_state), tuple(new_path))
        if result is not None:
            if min_path is None or len(result) < len(min_path):
                min_path = result
    return min_path

# initial state
initial_state = (['Red', 'Red', 'Blue', 'Red'], ['Red', 'Blue', 'Green', 'Blue'], ['Green', 'Green', 'Blue', 'Green'])

# goal state
goal_state = (['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red'],
              ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'],
              ['Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green'])

# convert the states to tuples
initial_state = tuple(tuple(tube) for tube in initial_state)
goal_state = tuple(tuple(tube) for tube in goal_state)

# find the shortest path
path = dfs(initial_state, ())

# print the result
print(path)
