
import heapq

def get_cost(from_stack, to_stack):
    cost = {0: 1, 1: 5, 2: 6, 3: 7, 4: 7, 5: 5}
    return cost[from_stack] + cost[to_stack]

def get_moves(stacks):
    moves = []
    for i, stack in enumerate(stacks):
        if stack:
            for j, to_stack in enumerate(stacks):
                if i != j and (not to_stack or to_stack[-1] == stack[-1]):
                    moves.append((i, j))
    return moves

def dfs(stacks, moves, cost):
    if all(len(set(stack)) <= 1 for stack in stacks if stack):
        return moves
    next_moves = get_moves(stacks)
    heapq.heapify(next_moves)
    while next_moves:
        from_stack, to_stack = heapq.heappop(next_moves)
        next_stacks = stacks[:]
        next_stacks[to_stack].append(next_stacks[from_stack].pop())
        next_cost = cost + get_cost(from_stack, to_stack)
        result = dfs(next_stacks, moves + [(from_stack, to_stack)], next_cost)
        if result is not None:
            return result

stacks = [['Yellow', 'Green', 'Green', 'Blue'], [], [], ['Red', 'Green', 'Blue', 'Yellow'], [], ['Yellow', 'Blue', 'Red', 'Red']]
print(dfs(stacks, [], 0))
