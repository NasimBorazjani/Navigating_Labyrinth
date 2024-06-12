
from collections import deque

def solve(state, goal, moves=[]):
    if state == goal:
        return moves
    for fr, to in [(0,1), (0,2), (1,0), (1,2), (2,0), (2,1)]:
        new_state = make_move(state, fr, to)
        if new_state not in visited:
            visited.add(tuple(new_state))
            result = solve(new_state, goal, [(fr, to)] + moves)
            if result:
                return result
    return None

def make_move(state, fr, to):
    if state[fr][-1] == state[to][-1] or state[to][-1] == state[to][-2]:
        new_state = state.copy()
        new_state[fr], new_state[to] = new_state[fr][:-1], new_state[fr][-1:] + new_state[to]
        return new_state
    return state

initial_state = [['Green', 'Red', 'Blue', 'Green'], ['Red', 'Blue', 'Red', 'Blue'], ['Red', 'Blue', 'Green', 'Green']]
goal_state = [['Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Red', 'Red'], ['Blue', 'Blue', 'Blue', 'Blue']]
visited = set()

result = solve(initial_state, goal_state)
print(result)
