
import heapq

def get_cost(from_stack, to_stack, costs):
    if len(to_stack) == 0 or to_stack[-1] == from_stack[-1]:
        return costs[len(to_stack)]
    return float('inf')

def get_moves(stacks, costs):
    moves = []
    for i, stack in enumerate(stacks):
        if len(stack) > 0:
            for j, to_stack in enumerate(stacks):
                if i != j:
                    cost = get_cost(stack, to_stack, costs)
                    if cost < float('inf'):
                        moves.append((cost, i, j))
    return moves

def restricted_sorting(stacks, costs):
    queue = [(0, stacks, [])]
    visited = set()
    while queue:
        cost, stacks, path = heapq.heappop(queue)
        state = tuple(tuple(stack) for stack in stacks)
        if state in visited:
            continue
        visited.add(state)
        if all(len(stack) == 0 or len(set(stack)) == 1 for stack in stacks):
            return path
        for move_cost, from_stack, to_stack in get_moves(stacks, costs):
            new_stacks = [list(stack) for stack in stacks]
            block = new_stacks[from_stack].pop()
            new_stacks[to_stack].append(block)
            new_path = path + [(from_stack, to_stack)]
            heapq.heappush(queue, (cost + move_cost, new_stacks, new_path))
    return []

stacks = [['Blue', 'Black', 'Yellow', 'Black', 'Red'], ['Blue', 'Blue', 'Green', 'Black', 'Yellow'], [], ['Yellow', 'Red', 'Red', 'Green', 'Green'], [], [], ['Red', 'Blue', 'Black', 'Green', 'Yellow'], []]
costs = {0: 7, 1: 5, 2: 7, 3: 2, 4: 6, 5: 7, 6: 5, 7: 3}
print(restricted_sorting(stacks, costs))
