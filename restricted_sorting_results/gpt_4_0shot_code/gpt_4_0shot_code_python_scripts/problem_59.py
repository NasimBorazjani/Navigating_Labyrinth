
import heapq

def get_cost(from_stack, to_stack, costs):
    if len(to_stack) == 0 or to_stack[-1] == from_stack[-1]:
        return costs[len(to_stack)]
    else:
        return float('inf')

def restricted_sorting(stacks, costs):
    visited = set()
    queue = [(0, stacks, [])]
    while queue:
        cost, stacks, moves = heapq.heappop(queue)
        state = tuple(tuple(stack) for stack in stacks)
        if state in visited:
            continue
        visited.add(state)
        if all(len(set(stack)) <= 1 for stack in stacks):
            return moves
        for i, from_stack in enumerate(stacks):
            if from_stack:
                for j, to_stack in enumerate(stacks):
                    if i != j and len(to_stack) < 5:
                        new_stacks = [list(stack) for stack in stacks]
                        new_stacks[j].append(new_stacks[i].pop())
                        new_cost = cost + get_cost(from_stack, to_stack, costs)
                        new_moves = moves + [(i, j)]
                        heapq.heappush(queue, (new_cost, new_stacks, new_moves))
    return []

stacks = [['Green', 'Blue', 'Green', 'Yellow', 'Yellow'], [], ['Red', 'Red', 'Green', 'Black', 'Black'], [], ['Blue', 'Yellow', 'Black', 'Yellow', 'Blue'], [], [], ['Black', 'Blue', 'Red', 'Red', 'Green']]
costs = {0: 1, 1: 5, 2: 5, 3: 4, 4: 8, 5: 6, 6: 8, 7: 9}
print(restricted_sorting(stacks, costs))
