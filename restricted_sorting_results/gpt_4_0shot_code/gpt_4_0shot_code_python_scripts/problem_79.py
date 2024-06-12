
from collections import deque
from copy import deepcopy

def restricted_sorting(stacks, costs):
    # Convert the stacks to a more convenient format
    stacks = [(list(reversed(stack)), i) for i, stack in enumerate(stacks)]
    # Initialize the BFS queue
    queue = deque([(stacks, [], 0)])
    # Initialize the minimum cost to infinity
    min_cost = float('inf')
    min_moves = None
    while queue:
        stacks, moves, cost = queue.popleft()
        if cost >= min_cost:
            continue
        # Check if the stacks are sorted
        if all(len(set(stack[0])) <= 1 for stack in stacks):
            if cost < min_cost:
                min_cost = cost
                min_moves = moves
            continue
        # Try all possible moves
        for i, (stack, stack_index) in enumerate(stacks):
            if stack:
                block = stack[-1]
                for j, (target_stack, target_index) in enumerate(stacks):
                    if i != j and (not target_stack or target_stack[-1] == block) and len(target_stack) < 7:
                        new_stacks = deepcopy(stacks)
                        new_stacks[i][0].pop()
                        new_stacks[j][0].append(block)
                        new_moves = moves + [(stack_index, target_index)]
                        new_cost = cost + costs[target_index]
                        queue.append((new_stacks, new_moves, new_cost))
    return min_moves

stacks = [['Red', 'Pink', 'Pink', 'Pink', 'Red', 'Black', 'Pink'], [], ['Green', 'Green', 'Blue', 'White', 'Yellow', 'Blue', 'Blue'], [], ['Green', 'Blue', 'White', 'Red', 'Blue', 'Black', 'Red'], ['Pink', 'White', 'Yellow', 'Black', 'Yellow', 'Green', 'White'], [], ['Red', 'Green', 'Black', 'White', 'Green', 'Red', 'Black'], [], [], ['Yellow', 'White', 'Yellow', 'Blue', 'Black', 'Yellow', 'Pink'], []]
costs = {0: 10, 1: 4, 2: 5, 3: 4, 4: 7, 5: 3, 6: 11, 7: 5, 8: 9, 9: 3, 10: 11, 11: 2}
print(restricted_sorting(stacks, costs))
