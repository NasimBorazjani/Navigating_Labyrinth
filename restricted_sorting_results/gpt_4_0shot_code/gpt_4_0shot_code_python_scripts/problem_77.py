
import heapq

def restricted_sorting(stacks, costs):
    # Initialize the priority queue with the initial state and cost 0
    queue = [(0, stacks, [])]

    # While there are states to process
    while queue:
        # Pop the state with the least cost
        cost, stacks, moves = heapq.heappop(queue)

        # If all stacks are sorted, return the moves
        if all(len(set(stack)) <= 1 for stack in stacks):
            return moves

        # For each pair of stacks
        for i in range(len(stacks)):
            for j in range(len(stacks)):
                # If the stacks are different and the move is valid
                if i != j and stacks[i] and (not stacks[j] or stacks[i][-1] == stacks[j][-1]):
                    # Make the move
                    new_stacks = [list(stack) for stack in stacks]
                    new_stacks[j].append(new_stacks[i].pop())
                    new_cost = cost + costs[j]

                    # Add the new state to the queue
                    new_moves = list(moves)
                    new_moves.append((i, j))
                    heapq.heappush(queue, (new_cost, new_stacks, new_moves))

# Test the function
stacks = [['Green', 'Black', 'White', 'Red', 'White', 'Yellow', 'Blue'], [], ['White', 'Pink', 'White', 'White', 'Green', 'Red', 'Blue'], [], ['Pink', 'Black', 'Black', 'White', 'Black', 'Green', 'Blue'], ['Pink', 'Green', 'Pink', 'Yellow', 'Yellow', 'Blue', 'Red'], [], ['Red', 'Yellow', 'Yellow', 'Yellow', 'Blue', 'Red', 'Black'], [], [], [], ['Red', 'Green', 'Black', 'Blue', 'Pink', 'Pink', 'Green']]
costs = {0: 13, 1: 5, 2: 8, 3: 11, 4: 6, 5: 9, 6: 5, 7: 11, 8: 2, 9: 11, 10: 11, 11: 7}
print(restricted_sorting(stacks, costs))
