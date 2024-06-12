
import heapq

def restricted_sorting(stacks, costs):
    # Initialize the priority queue with the initial state and cost 0
    queue = [(0, stacks, [])]
    # Initialize the set of visited states
    visited = set()
    # While there are states to process
    while queue:
        # Pop the state with the least cost
        cost, stacks, moves = heapq.heappop(queue)
        # Convert the state to a tuple to be able to store it in a set
        state = tuple(tuple(stack) for stack in stacks)
        # If this state has been visited before, skip it
        if state in visited:
            continue
        # Mark this state as visited
        visited.add(state)
        # If this state is a goal state, return the moves that lead to it
        if all(len(set(stack)) <= 1 for stack in stacks if stack):
            return moves
        # For each possible move
        for i in range(len(stacks)):
            for j in range(len(stacks)):
                # If the move is valid
                if i != j and stacks[i] and (not stacks[j] or stacks[i][-1] == stacks[j][-1]) and len(stacks[j]) < 6:
                    # Perform the move
                    new_stacks = [list(stack) for stack in stacks]
                    new_stacks[j].append(new_stacks[i].pop())
                    new_moves = list(moves)
                    new_moves.append((i, j))
                    # Add the new state to the queue with its cost
                    heapq.heappush(queue, (cost + costs[j], new_stacks, new_moves))

# Test the function
stacks = [[], [], ['Green', 'Red', 'White', 'Green', 'Black', 'White'], [], ['Red', 'Red', 'Yellow', 'White', 'Blue', 'Black'], ['Blue', 'Yellow', 'Red', 'Blue', 'Blue', 'Green'], [], [], ['Black', 'White', 'Black', 'White', 'Yellow', 'Blue'], ['Yellow', 'Black', 'Green', 'Red', 'Green', 'Yellow']]
costs = {0: 7, 1: 11, 2: 8, 3: 10, 4: 5, 5: 6, 6: 10, 7: 10, 8: 4, 9: 11}
print(restricted_sorting(stacks, costs))
