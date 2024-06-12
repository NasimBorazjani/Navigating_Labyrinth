
from collections import deque

# Define the colors and the goal state
colors = ['Red', 'Green', 'Blue']
goal_state = [
    [color]*3 for color in colors
]

# Function to check if a state is the goal state
def is_goal_state(state):
    return state == goal_state

# Function to generate all possible next states
def next_states(state):
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[i][0] != state[j][0] and len(state[j]) < 9:
                new_state = [list(tube) for tube in state]
                ball = new_state[i].pop(0)
                new_state[j].append(ball)
                move = (i, j)
                yield (new_state, move)

# Use DFS to find the shortest sequence of moves
def dfs(state, path=[]):
    if is_goal_state(state):
        return path
    for new_state, move in next_states(state):
        result = dfs(new_state, path + [move])
        if result is not None:
            return result

# Define the initial state
initial_state = [
    ['Red', 'Green', 'Red', 'Blue', 'Blue', 'Green'],
    ['Green', 'Green', 'Red', 'Red', 'Blue', 'Blue'],
    ['Blue', 'Red', 'Green', 'Blue', 'Green', 'Red']
]

# Find the shortest sequence of moves
moves = dfs(initial_state)
print(moves)
