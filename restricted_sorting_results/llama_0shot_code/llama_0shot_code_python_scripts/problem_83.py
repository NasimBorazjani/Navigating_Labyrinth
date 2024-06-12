
import heapq

def restricted_sorting(stacks, costs):
    # Initialize a priority queue with the empty stacks
    queue = [(-costs[i], i) for i in range(len(stacks)) if len(stacks[i]) == 0]
    heapq.heapify(queue)

    # Initialize the transfer pairs
    transfers = []

    # Iterate over the non-empty stacks
    for i in range(len(stacks)):
        if stacks[i]:
            # Pop a block from the stack
            block = stacks[i].pop()

            # Find the stack with the minimum cost
            while queue:
                cost, j = heapq.heappop(queue)
                cost = -cost

                # If the stack is not full, push the block to the stack
                if len(stacks[j]) < 7:
                    stacks[j].append(block)
                    transfers.append((i, j))
                    break

                # If the stack is full, push the block back to the queue
                else:
                    heapq.heappush(queue, (-cost, j))

    return transfers

# Test the function
stacks = [[], ['Black', 'Green', 'White', 'Pink', 'Yellow', 'Blue', 'Red'], [], ['Green', 'Red', 'Red', 'Red', 'White', 'Black', 'Black'], [], ['Blue', 'Blue', 'Pink', 'Yellow', 'Pink', 'Green', 'Red'], ['Blue', 'Black', 'White', 'Green', 'White', 'Yellow', 'Yellow'], ['White', 'Blue', 'Pink', 'Green', 'Yellow', 'Green', 'Pink'], [], ['Yellow', 'Black', 'White', 'Red', 'Blue', 'Black', 'Pink'], [], []]
costs = [10, 8, 12, 3, 5, 11, 5, 12, 3, 3, 11, 6]
print(restricted_sorting(stacks, costs))
