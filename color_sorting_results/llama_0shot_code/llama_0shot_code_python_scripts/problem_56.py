
from collections import deque

# Define the colors and the goal state
colors = ['Green', 'Red', 'Blue']
goal_state = [['Green', 'Green', 'Green', 'Green', 'Green', 'Red', 'Red', 'Red'], 
              ['Red', 'Red', 'Red', 'Red', 'Red', 'Blue', 'Blue', 'Blue'], 
              ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Green', 'Green', 'Green']]

# Check if a state is the goal state
def is_goal_state(state):
    return state == goal_state

# Generate all possible next states
def next_states(state):
    states = []
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if len(state[i]) < 8 and len(state[j]) < 8:
                new_state = [list(x) for x in state]
                ball = new_state[i].pop()
                new_state[j].append(ball)
                states.append(((i, j), new_state))
    return states

# DFS function
def dfs(state):
    if is_goal_state(state):
        return []
    for i, new_state in next_states(state):
        result = dfs(new_state)
        if result is not None:
            return [i] + result

# Test the function with the initial state
initial_state = [['Green', 'Red', 'Green', 'Blue', 'Red'], 
                 ['Red', 'Green', 'Red', 'Blue', 'Blue'], 
                 ['Green', 'Blue', 'Red', 'Green', 'Blue']]

print(dfs(initial_state))
