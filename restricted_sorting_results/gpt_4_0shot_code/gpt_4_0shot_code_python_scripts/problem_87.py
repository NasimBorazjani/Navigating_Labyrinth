
import heapq

def restricted_sorting(stacks, costs):
    # Initialize the priority queue with the initial state and cost 0
    queue = [(0, stacks, [])]

    # While there are states in the queue
    while queue:
        # Pop the state with the least cost
        cost, stacks, moves = heapq.heappop(queue)

        # If all stacks are sorted, return the moves
        if all(len(set(stack)) <= 1 for stack in stacks if stack):
            return moves

        # For each pair of stacks
        for i in range(len(stacks)):
            for j in range(len(stacks)):
                # If the stacks are different and the first stack is not empty
                if i != j and stacks[i]:
                    # If the second stack is empty or the top block of the first stack is the same color as the top block of the second stack
                    if not stacks[j] or stacks[i][-1] == stacks[j][-1]:
                        # Create a new state by moving a block from the first stack to the second stack
                        new_stacks = [list(stack) for stack in stacks]
                        new_stacks[j].append(new_stacks[i].pop())

                        # Add the new state to the queue with the cost of the move
                        new_cost = cost + costs[j]
                        new_moves = moves + [(i, j)]
                        heapq.heappush(queue, (new_cost, new_stacks, new_moves))

# Test the function
stacks = [['Black', 'Blue', 'Pink', 'Green', 'Blue', 'Red', 'Red'], ['Yellow', 'White', 'White', 'Black', 'Yellow', 'Green', 'Green'], ['Yellow', 'Pink', 'White', 'Pink', 'Black', 'Red', 'Black'], [], ['Pink', 'Red', 'Blue', 'White', 'Blue', 'Blue', 'Red'], ['Blue', 'Yellow', 'White', 'Pink', 'Pink', 'Green', 'Green'], [], [], ['Yellow', 'Black', 'Yellow', 'White', 'Red', 'Black', 'Green'], [], [], []]
costs = {0: 11, 1: 13, 2: 4, 3: 4, 4: 13, 5: 7, 6: 12, 7: 6, 8: 4, 9: 6, 10: 11, 11: 4}
print(restricted_sorting(stacks, costs))
