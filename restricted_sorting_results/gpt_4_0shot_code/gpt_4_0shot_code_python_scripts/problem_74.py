
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
                    # If the second stack is empty or the top block of the first stack is the same color as the top block of the second stack
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
stacks = [['Black', 'Blue', 'Red', 'White', 'Red', 'Green'], ['Red', 'Black', 'Red', 'Green', 'Blue', 'Black'], ['Black', 'Yellow', 'Yellow', 'White', 'White', 'Yellow'], [], [], ['White', 'Green', 'Green', 'Red', 'Green', 'Yellow'], [], ['Blue', 'Blue', 'Blue', 'Black', 'White', 'Yellow'], [], []]
costs = {0: 3, 1: 8, 2: 5, 3: 10, 4: 8, 5: 2, 6: 3, 7: 4, 8: 11, 9: 3}
print(restricted_sorting(stacks, costs))
