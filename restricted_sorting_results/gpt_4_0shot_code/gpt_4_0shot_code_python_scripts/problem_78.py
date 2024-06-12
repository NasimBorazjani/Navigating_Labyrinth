
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
                # If the first stack is not empty and the second stack can accept the top block of the first stack
                if stacks[i] and (not stacks[j] or stacks[i][-1] == stacks[j][-1]):
                    # Create a new state by moving the top block from the first stack to the second stack
                    new_stacks = [list(stack) for stack in stacks]
                    new_stacks[j].append(new_stacks[i].pop())

                    # Calculate the new cost
                    new_cost = cost + costs[j]

                    # Add the new state to the queue
                    heapq.heappush(queue, (new_cost, new_stacks, moves + [(i, j)]))

# Test the function
stacks = [[], ['Blue', 'Pink', 'Red', 'Red', 'Yellow', 'White', 'Green'], [], [], ['White', 'Black', 'Blue', 'Yellow', 'Yellow', 'Pink', 'White'], ['Green', 'Pink', 'White', 'Blue', 'Pink', 'Red', 'Pink'], ['Black', 'Green', 'Yellow', 'White', 'Yellow', 'Red', 'Blue'], [], ['Red', 'White', 'Black', 'Blue', 'Black', 'Yellow', 'Green'], [], ['Green', 'Black', 'Pink', 'Black', 'Red', 'Green', 'Blue'], []]
costs = {0: 2, 1: 7, 2: 5, 3: 11, 4: 6, 5: 13, 6: 12, 7: 7, 8: 8, 9: 6, 10: 7, 11: 7}
print(restricted_sorting(stacks, costs))
