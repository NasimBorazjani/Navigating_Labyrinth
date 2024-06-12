
import heapq

def restricted_sorting(stacks, costs):
    # Initialize the priority queue with the initial state and cost 0
    queue = [(0, stacks, [])]

    # While there are states in the queue
    while queue:
        # Pop the state with the least cost
        cost, stacks, moves = heapq.heappop(queue)

        # If all stacks are sorted, return the moves
        if all(len(set(stack)) <= 1 for stack in stacks):
            return moves

        # For each pair of stacks
        for i in range(len(stacks)):
            for j in range(len(stacks)):
                # If the stacks are different and the first stack is not empty
                if i != j and stacks[i]:
                    # If the second stack is empty or the top block is the same color
                    if not stacks[j] or stacks[i][-1] == stacks[j][-1]:
                        # Copy the stacks and make the move
                        new_stacks = [list(stack) for stack in stacks]
                        new_stacks[j].append(new_stacks[i].pop())

                        # Calculate the new cost
                        new_cost = cost + costs[j]

                        # Add the new state to the queue
                        new_moves = list(moves)
                        new_moves.append((i, j))
                        heapq.heappush(queue, (new_cost, new_stacks, new_moves))

# Test the function
stacks = [['Black', 'Black', 'Yellow', 'Blue', 'Black', 'Black', 'Green'], [], ['Blue', 'Yellow', 'Green', 'Black', 'White', 'White', 'Blue'], ['Red', 'White', 'Pink', 'White', 'Pink', 'Green', 'Pink'], ['Green', 'Blue', 'Black', 'Green', 'Red', 'Green', 'Yellow'], [], [], ['Red', 'White', 'Blue', 'Yellow', 'Blue', 'White', 'Red'], ['Yellow', 'Yellow', 'Red', 'Pink', 'Red', 'Pink', 'Pink'], [], [], []]
costs = {0: 10, 1: 7, 2: 7, 3: 7, 4: 9, 5: 3, 6: 8, 7: 5, 8: 4, 9: 10, 10: 7, 11: 7}
print(restricted_sorting(stacks, costs))
