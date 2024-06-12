
from collections import defaultdict
from heapq import heappop, heappush

def solve(stacks, costs):
    # Create a priority queue with the initial state and cost 0
    queue = [(0, stacks, [])]
    # Create a set to store visited states
    visited = set()
    # Create a dictionary to store the minimum cost to reach each state
    min_cost = defaultdict(lambda: float('inf'))
    min_cost[tuple(map(tuple, stacks))] = 0

    while queue:
        # Pop the state with the lowest cost
        cost, stacks, moves = heappop(queue)
        # If this state has been visited before, skip it
        if tuple(map(tuple, stacks)) in visited:
            continue
        visited.add(tuple(map(tuple, stacks)))
        # If all stacks are sorted, return the moves
        if all(len(set(stack)) <= 1 for stack in stacks if stack):
            return moves
        # Try all possible moves
        for i, stack in enumerate(stacks):
            if stack:
                for j, target in enumerate(stacks):
                    if i != j and (not target or target[-1] == stack[-1]) and len(target) < 7:
                        # Make the move
                        new_stacks = [list(s) for s in stacks]
                        new_stacks[j].append(new_stacks[i].pop())
                        new_cost = cost + costs[j]
                        # If the new cost is less than the minimum cost to reach this state, update it
                        if new_cost < min_cost[tuple(map(tuple, new_stacks))]:
                            min_cost[tuple(map(tuple, new_stacks))] = new_cost
                            # Add the new state to the queue
                            heappush(queue, (new_cost, new_stacks, moves + [(i, j)]))

# Test the function
stacks = [['Black', 'Blue', 'Green', 'Green', 'Pink', 'Black', 'Red'], [], ['Green', 'White', 'Yellow', 'Red', 'White', 'Blue', 'Pink'], [], [], ['Black', 'Green', 'Black', 'Yellow', 'Black', 'Blue', 'Black'], ['Green', 'Blue', 'Yellow', 'Yellow', 'Red', 'Yellow', 'Pink'], ['Red', 'White', 'Blue', 'Pink', 'Red', 'Blue', 'White'], [], [], ['Red', 'White', 'Pink', 'Green', 'Yellow', 'White', 'Pink'], []]
costs = {0: 7, 1: 9, 2: 13, 3: 3, 4: 4, 5: 4, 6: 6, 7: 11, 8: 12, 9: 3, 10: 13, 11: 5}
print(solve(stacks, costs))
