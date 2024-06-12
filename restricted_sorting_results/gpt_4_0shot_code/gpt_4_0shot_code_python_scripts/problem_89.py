
import heapq

def restricted_sorting(stacks, costs):
    # Initialize the priority queue with the initial state and cost 0
    queue = [(0, stacks, [])]

    # Keep track of visited states to avoid cycles
    visited = set()

    while queue:
        # Pop the state with the least cost
        cost, stacks, moves = heapq.heappop(queue)

        # Convert the state to a tuple to be able to store it in a set
        state = tuple(tuple(stack) for stack in stacks)

        # If we have already visited this state, skip it
        if state in visited:
            continue

        # Mark the state as visited
        visited.add(state)

        # If all stacks are sorted, return the moves
        if all(len(set(stack)) <= 1 for stack in stacks if stack):
            return moves

        # Try all possible moves
        for i, stack in enumerate(stacks):
            if stack:  # If the stack is not empty
                for j, target in enumerate(stacks):
                    if i != j and (not target or target[-1] == stack[-1]):  # If the target stack is empty or has the same color on top
                        # Make a copy of the stacks and the move
                        new_stacks = [list(s) for s in stacks]
                        new_stacks[j].append(new_stacks[i].pop())
                        new_moves = list(moves)
                        new_moves.append((i, j))

                        # Push the new state to the queue with the updated cost
                        new_cost = cost + costs[j]
                        heapq.heappush(queue, (new_cost, new_stacks, new_moves))

# Test the function
stacks = [[], ['Blue', 'Yellow', 'Pink', 'Green', 'Pink', 'Red', 'Red'], [], ['Pink', 'White', 'Pink', 'Black', 'White', 'Black', 'Pink'], ['Yellow', 'Green', 'White', 'Red', 'Yellow', 'Yellow', 'Red'], ['Green', 'Pink', 'White', 'Blue', 'Red', 'White', 'Red'], [], [], ['Blue', 'Blue', 'Yellow', 'Blue', 'Black', 'Blue', 'Green'], ['Yellow', 'Black', 'Black', 'White', 'Green', 'Green', 'Black'], [], []]
costs = {0: 10, 1: 8, 2: 6, 3: 4, 4: 11, 5: 5, 6: 11, 7: 5, 8: 7, 9: 7, 10: 10, 11: 10}
print(restricted_sorting(stacks, costs))
