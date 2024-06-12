
from collections import deque
from copy import deepcopy

def get_moves(state):
    moves = []
    for i in range(8):
        if state[i]:
            for j in range(8):
                if i != j and (not state[j] or state[j][-1] == state[i][-1]) and len(state[j]) < 5:
                    moves.append((i, j))
    return moves

def bfs(initial_state):
    queue = deque([initial_state])
    costs = {initial_state: 0}
    prev = {initial_state: None}
    move_cost = {0: 7, 1: 2, 2: 1, 3: 1, 4: 9, 5: 4, 6: 2, 7: 7}
    while queue:
        state = queue.popleft()
        for move in get_moves(state):
            new_state = deepcopy(state)
            new_state[move[1]].append(new_state[move[0]].pop())
            cost = costs[state] + move_cost[move[1]]
            if new_state not in costs or cost < costs[new_state]:
                costs[new_state] = cost
                prev[new_state] = (state, move)
                queue.append(new_state)
    return costs, prev

def get_solution(costs, prev):
    state = min(costs, key=costs.get)
    solution = []
    while prev[state]:
        solution.append(prev[state][1])
        state = prev[state][0]
    return solution[::-1]

initial_state = [[], [], ['Yellow', 'Yellow', 'Green', 'Black', 'Red'], ['Black', 'Green', 'Black', 'Blue', 'Yellow'], ['Green', 'Blue', 'Yellow', 'Red', 'Blue'], [], [], ['Black', 'Red', 'Green', 'Red', 'Blue']]
initial_state = tuple(tuple(stack) for stack in initial_state)
costs, prev = bfs(initial_state)
solution = get_solution(costs, prev)
print(solution)
