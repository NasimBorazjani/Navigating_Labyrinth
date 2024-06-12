
import heapq

def restricted_sorting(stacks, costs):
    # Initialize the priority queue with the initial state and cost 0
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
                    if i != j and (not target or target[-1] == stack[-1]) and len(target) < 5:
                        new_stacks = [list(s) for s in stacks]
                        new_stacks[j].append(new_stacks[i].pop())
                        new_moves = moves + [(i, j)]
                        new_cost = cost + costs[j]
                        heapq.heappush(queue, (new_cost, new_stacks, new_moves))

# Test the function
stacks = [[], ['Blue', 'Green', 'Red', 'Yellow', 'Blue'], ['Green', 'Blue', 'Yellow', 'Black', 'Red'], [], ['Red', 'Yellow', 'Yellow', 'Black', 'Black'], ['Green', 'Blue', 'Green', 'Black', 'Red'], [], []]
costs = {0: 7, 1: 4, 2: 1, 3: 2, 4: 6, 5: 8, 6: 7, 7: 6}
print(restricted_sorting(stacks, costs))
