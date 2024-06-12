
import numpy as np

def find_blank_8p(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == '_':
                return i, j

def actions_f_8p(state):
    actions = ['left', 'right', 'up', 'down']
    i, j = find_blank_8p(state)
    if i == 0:
        actions.remove('up')
    if i == len(state) - 1:
        actions.remove('down')
    if j == 0:
        actions.remove('left')
    if j == len(state[i]) - 1:
        actions.remove('right')
    return actions

def take_action_f_8p(state, action):
    i, j = find_blank_8p(state)
    state_copy = [row.copy() for row in state]
    if action == 'up':
        state_copy[i][j], state_copy[i-1][j] = state_copy[i-1][j], state_copy[i][j]
    elif action == 'down':
        state_copy[i][j], state_copy[i+1][j] = state_copy[i+1][j], state_copy[i][j]
    elif action == 'left':
        state_copy[i][j], state_copy[i][j-1] = state_copy[i][j-1], state_copy[i][j]
    elif action == 'right':
        state_copy[i][j], state_copy[i][j+1] = state_copy[i][j+1], state_copy[i][j]
    return state_copy

def goal_test_f_8p(state, goal):
    return state == goal

def solve_8p(initial_state, goal_state):
    state = initial_state
    solution = []
    while not goal_test_f_8p(state, goal_state):
        actions = actions_f_8p(state)
        best_action = None
        best_heuristic = float('inf')
        for action in actions:
            new_state = take_action_f_8p(state, action)
            heuristic = np.sum(np.abs(np.array(new_state) - np.array(goal_state)))
            if heuristic < best_heuristic:
                best_heuristic = heuristic
                best_action = action
        state = take_action_f_8p(state, best_action)
        i, j = find_blank_8p(state)
        solution.append(state[i][j])
    return solution

initial_state = [[46, 82, 90], [36, 41, 38], [28, 55, '_']]
goal_state = [[90, 82, 46], [55, 41, 36], [38, 28, '_']]
print(solve_8p(initial_state, goal_state))
