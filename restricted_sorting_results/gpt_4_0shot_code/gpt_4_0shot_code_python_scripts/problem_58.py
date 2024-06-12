
import heapq

def get_moves(state):
    for i, stack in enumerate(state):
        if stack:
            for j, target in enumerate(state):
                if i != j and (not target or target[-1] == stack[-1]):
                    yield (i, j)

def get_cost(move, costs):
    return costs[move[1]]

def solve(state, costs):
    heap = [(0, state, [])]
    seen = set()

    while heap:
        cost, state, moves = heapq.heappop(heap)
        serialized = str(state)
        if serialized in seen:
            continue
        seen.add(serialized)

        if all(len(set(stack)) <= 1 for stack in state if stack):
            return moves

        for move in get_moves(state):
            new_state = state[:]
            new_state[move[1]] = new_state[move[1]] + [new_state[move[0]].pop()]
            new_moves = moves + [move]
            new_cost = cost + get_cost(move, costs)
            heapq.heappush(heap, (new_cost, new_state, new_moves))

stacks = [[], ['Green', 'Yellow', 'Red', 'Red', 'Red'], [], ['Green', 'Yellow', 'Green', 'Blue', 'Black'], ['Red', 'Yellow', 'Black', 'Blue', 'Black'], [], [], ['Green', 'Black', 'Yellow', 'Blue', 'Blue']]
costs = {0: 4, 1: 8, 2: 9, 3: 9, 4: 5, 5: 7, 6: 9, 7: 6}

print(solve(stacks, costs))
