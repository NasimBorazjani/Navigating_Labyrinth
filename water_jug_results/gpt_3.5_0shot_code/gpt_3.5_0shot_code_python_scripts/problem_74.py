
from itertools import permutations

# Function to check if the current state is valid
def is_valid(state):
    for i in range(1, len(state)):
        if state[i] < state[i-1]:
            return False
    return True

# Function to generate all possible actions
def generate_actions(jugs, buckets):
    actions = []
    for jug in jugs:
        for bucket in range(len(buckets)):
            actions.append(('+', jug, bucket))
            actions.append(('-', jug, bucket))
    return actions

# Function to apply an action to the current state
def apply_action(state, action):
    new_state = list(state)
    op, jug, bucket = action
    if op == '+':
        new_state[bucket] += jug
    elif op == '-':
        new_state[bucket] -= jug
    return tuple(new_state)

# Function to solve the problem using backtracking
def solve(jugs, buckets, target):
    actions = generate_actions(jugs, buckets)
    min_actions = float('inf')
    min_solution = None

    for perm in permutations(jugs):
        state = (0, 0, 0, 0)
        visited = set()
        stack = [(state, [])]

        while stack:
            current_state, current_actions = stack.pop()

            if current_state == target:
                if len(current_actions) < min_actions:
                    min_actions = len(current_actions)
                    min_solution = current_actions
                continue

            if len(current_actions) >= min_actions:
                continue

            for action in actions:
                new_state = apply_action(current_state, action)
                if new_state not in visited and is_valid(new_state):
                    visited.add(new_state)
                    stack.append((new_state, current_actions + [action]))

    return min_solution

# Given data
jugs = [91, 141, 56, 65, 89, 40, 39, 92]
buckets = [294, 375, 459, 466]

# Solve the problem
solution = solve(jugs, buckets, tuple(buckets))
print(solution)
