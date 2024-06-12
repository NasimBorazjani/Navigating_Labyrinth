
from collections import deque

# Define the colors and the goal state
colors = ['Blue', 'Red', 'Green']
goal = [['Blue']*6, ['Red']*6, ['Green']*6]

# Function to check if a state is the goal state
def is_goal(state):
    return state == goal

# Function to generate all possible next states
def next_states(state):
    states = []
    for i in range(len(state)):
        if state[i]: # if this tube is not empty
            color = state[i][-1] # get the color of the top ball
            for j in range(len(state)):
                if j != i and len(state[j]) < 9: # cannot move to a full tube
                    new_state = [b[:] for b in state]
                    new_state[i].pop() # remove the top ball from the source tube
                    new_state[j].append(color) # add the top ball to the target tube
                    states.append(((i, j), new_state))
    return states

# Use DFS to find the shortest sequence of moves
def dfs(state, path=[]):
    if is_goal(state):
        return path
    for i, new_state in next_states(state):
        result = dfs(new_state, path + [i])
        if result:
            return result

# Define the initial state
initial_state = [['Blue', 'Red', 'Blue', 'Red', 'Blue', 'Red'], 
                 ['Blue', 'Blue', 'Red', 'Green', 'Green', 'Green'], 
                 ['Green', 'Red', 'Green', 'Blue', 'Green', 'Red']]

# Find the shortest sequence of moves
moves = dfs(initial_state)
print(moves)
