
import heapq

def restricted_sorting(stacks, costs):
    # Create a priority queue with the initial state and cost 0
    queue = [(0, stacks, [])]
    visited = set()

    while queue:
        # Pop the state with the least cost
        cost, stacks, moves = heapq.heappop(queue)
        state = tuple(tuple(stack) for stack in stacks)

        # If this state has been visited before, skip it
        if state in visited:
            continue
        visited.add(state)

        # If all stacks are sorted, return the moves
        if all(len(set(stack)) <= 1 for stack in stacks):
            return moves

        # Try all possible moves
        for i, stack in enumerate(stacks):
            if stack:
                for j, target in enumerate(stacks):
                    if i != j and (not target or target[-1] == stack[-1]) and len(target) < 6:
                        new_stacks = [list(s) for s in stacks]
                        new_stacks[j].append(new_stacks[i].pop())
                        new_moves = moves + [(i, j)]
                        new_cost = cost + costs[j]
                        heapq.heappush(queue, (new_cost, new_stacks, new_moves))

# Test the function
stacks = [
    ['Black', 'Red', 'Black', 'Green', 'Blue', 'Yellow'],
    ['Yellow', 'Yellow', 'Black', 'Blue', 'Red', 'Green'],
    [], [], [], [],
    ['Yellow', 'Black', 'White', 'Yellow', 'Red', 'Black'],
    ['Green', 'Blue', 'Green', 'White', 'Blue', 'Green'],
    ['Red', 'White', 'Blue', 'White', 'White', 'Red'],
    []
]
costs = {0: 11, 1: 8, 2: 4, 3: 6, 4: 4, 5: 3, 6: 6, 7: 9, 8: 5, 9: 10}
print(restricted_sorting(stacks, costs))
