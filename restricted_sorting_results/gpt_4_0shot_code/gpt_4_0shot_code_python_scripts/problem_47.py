
import heapq

def get_cost(from_stack, to_stack, costs):
    if len(to_stack) == 0 or to_stack[-1] == from_stack[-1]:
        return costs[len(to_stack)]
    else:
        return float('inf')

def restricted_sorting(stacks, costs):
    visited = set()
    moves = []
    queue = [(0, stacks, moves)]
    while queue:
        cost, stacks, moves = heapq.heappop(queue)
        state = tuple(tuple(stack) for stack in stacks)
        if state in visited:
            continue
        visited.add(state)
        if all(len(stack) == 0 or len(stack) == 4 and len(set(stack)) == 1 for stack in stacks):
            return moves
        for i, from_stack in enumerate(stacks):
            if len(from_stack) > 0:
                for j, to_stack in enumerate(stacks):
                    if i != j and len(to_stack) < 5:
                        new_stacks = [list(stack) for stack in stacks]
                        new_stacks[j].append(new_stacks[i].pop())
                        new_moves = list(moves)
                        new_moves.append((i, j))
                        new_cost = cost + get_cost(from_stack, to_stack, costs)
                        heapq.heappush(queue, (new_cost, new_stacks, new_moves))
    return []

stacks = [[], [], ['Red', 'Yellow', 'Black', 'Yellow', 'Green'], ['Red', 'Red', 'Blue', 'Red', 'Black'], [], ['Black', 'Blue', 'Yellow', 'Blue', 'Black'], [], ['Green', 'Green', 'Yellow', 'Blue', 'Green']]
costs = {0: 4, 1: 6, 2: 8, 3: 2, 4: 4, 5: 7, 6: 7, 7: 5}
print(restricted_sorting(stacks, costs))
