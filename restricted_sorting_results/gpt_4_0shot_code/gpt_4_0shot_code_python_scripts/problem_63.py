
import heapq

def restricted_sorting(stacks, costs):
    # Initialize the priority queue with the initial state and cost 0
    queue = [(0, stacks, [])]
    # Set of visited states
    visited = set()
    # While there are states to process
    while queue:
        # Pop the state with the least cost
        cost, stacks, moves = heapq.heappop(queue)
        # Convert the current state to a tuple to be able to store it in a set
        state = tuple(tuple(stack) for stack in stacks)
        # If this state has been visited before, skip it
        if state in visited:
            continue
        # Mark this state as visited
        visited.add(state)
        # If this state is a goal state, return the moves that lead to it
        if all(len(set(stack)) <= 1 for stack in stacks if stack):
            return moves
        # For each pair of stacks
        for i in range(len(stacks)):
            for j in range(len(stacks)):
                # If the stack is not empty and the block can be moved
                if stacks[i] and (not stacks[j] or stacks[i][-1] == stacks[j][-1]) and i != j:
                    # Create a new state by moving the block
                    new_stacks = [list(stack) for stack in stacks]
                    new_stacks[j].append(new_stacks[i].pop())
                    # Calculate the cost of the move
                    new_cost = cost + costs[j]
                    # Add the new state to the queue
                    heapq.heappush(queue, (new_cost, new_stacks, moves + [(i, j)]))

# Test the function
stacks = [[], [], ['Blue', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Black'], ['Red', 'Red', 'Blue', 'White', 'Blue', 'Black'], ['White', 'Green', 'Red', 'Black', 'Blue', 'Yellow'], [], ['White', 'Green', 'Green', 'White', 'Green', 'Green'], ['Black', 'Red', 'Red', 'Blue', 'White', 'Black'], [], []]
costs = {0: 7, 1: 7, 2: 8, 3: 5, 4: 8, 5: 10, 6: 5, 7: 5, 8: 4, 9: 8}
print(restricted_sorting(stacks, costs))
