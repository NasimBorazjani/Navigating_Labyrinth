
from collections import defaultdict
from heapq import heappop, heappush

def solve(stacks, costs):
    # Create a dictionary to store the cost of moving a block to each stack
    cost_dict = defaultdict(int)
    for i, stack in enumerate(stacks):
        if stack:
            cost_dict[stack[-1]] = min(cost_dict[stack[-1]], costs[i]) if stack[-1] in cost_dict else costs[i]

    # Create a priority queue to store the possible moves
    queue = [(0, stacks, [])]
    visited = set()

    while queue:
        cost, stacks, moves = heappop(queue)
        state = tuple(tuple(stack) for stack in stacks)
        if state in visited:
            continue
        visited.add(state)

        # Check if all stacks are sorted
        if all(len(set(stack)) <= 1 for stack in stacks):
            return moves

        for i, stack1 in enumerate(stacks):
            if stack1:
                for j, stack2 in enumerate(stacks):
                    if i != j and (not stack2 or stack1[-1] == stack2[-1]) and len(stack2) < 7:
                        new_stacks = [list(stack) for stack in stacks]
                        new_stacks[j].append(new_stacks[i].pop())
                        new_moves = moves + [(i, j)]
                        new_cost = cost + costs[j]
                        heappush(queue, (new_cost, new_stacks, new_moves))

    return []

stacks = [['Red', 'Black', 'Yellow', 'Black', 'White', 'Blue', 'White'], [], ['White', 'Blue', 'Green', 'Yellow', 'Blue', 'Yellow', 'Pink'], ['Yellow', 'Red', 'Pink', 'Green', 'Black', 'Red', 'White'], [], ['Pink', 'Red', 'Green', 'Green', 'Green', 'Black', 'Blue'], ['Pink', 'Blue', 'Blue', 'Black', 'Red', 'Pink', 'Black'], ['Yellow', 'Red', 'Pink', 'White', 'White', 'Yellow', 'Green'], [], [], [], []]
costs = {0: 7, 1: 13, 2: 10, 3: 12, 4: 4, 5: 13, 6: 2, 7: 11, 8: 11, 9: 10, 10: 8, 11: 9}

print(solve(stacks, costs))
