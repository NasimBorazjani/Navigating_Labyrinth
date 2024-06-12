
from collections import deque

def solve(state, goal, moves=[]):
    if state == goal:
        return moves
    for fr, to in possible_moves(state):
        new_state = make_move(state, fr, to)
        result = solve(new_state, goal, [(*fr, *to), *moves])
        if result:
            return result
    return None

def possible_moves(state):
    for i, tube in enumerate(state):
        for j, tube2 in enumerate(state):
            if i != j and len(tube2) < 6:
                yield (i, tube[0]), (j, tube2[-1])

def make_move(state, fr, to):
    new_state = state[:]
    new_state[fr[0]].pop(0)
    new_state[to[0]].append(to[1])
    return new_state

def main():
    initial_state = [['Green', 'Blue', 'Red', 'Red'], ['Red', 'Green', 'Green', 'Blue'], ['Red', 'Green', 'Blue', 'Blue']]
    goal_state = [['Red', 'Red', 'Red'], ['Green', 'Green', 'Green'], ['Blue', 'Blue', 'Blue']]
    for tube in initial_state:
        tube.sort()
    for tube in goal_state:
        tube.sort()
    result = solve(initial_state, goal_state)
    print(result)

if __name__ == "__main__":
    main()
