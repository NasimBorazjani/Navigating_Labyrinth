
from collections import deque

def get_moves(state):
    moves = []
    for from_tube in range(len(state)):
        if state[from_tube]:  # if the tube is not empty
            for to_tube in range(len(state)):
                if from_tube != to_tube and len(state[to_tube]) < 6:  # valid move
                    moves.append((from_tube, to_tube))
    return moves

def dfs(state, path):
    if not state:  # goal state
        return path
    for move in get_moves(state):
        new_state = deque(state)
        ball = new_state[move[0]].pop()  # move the ball
        new_state[move[1]].append(ball)
        result = dfs(list(new_state), path + [move])  # recursive call
        if result:  # if a solution is found
            return result

# initial state
initial_state = [deque(["Blue", "Green", "Blue", "Red"]), deque(["Red", "Blue", "Green", "Red"]), deque(["Green", "Green", "Blue", "Red"])]

# solve the problem
solution = dfs(initial_state, [])
print(solution)
