
import heapq

def restricted_sorting(stacks, costs):
    # Create a priority queue with stacks and their current costs
    queue = [(-costs[i], i) for i in range(len(stacks))]
    # List of final sorted stacks
    sorted_stacks = [[] for _ in range(len(stacks))]
    # List of transfer pairs with their costs
    transfers = []

    while queue:
        # Get the stack with the least cost
        cost, index = heapq.heappop(queue)
        # Get the top block from the current stack
        block = stacks[index].pop()
        # Find the best destination stack for the current block
        destination = None
        for i, stack in enumerate(sorted_stacks):
            if not stack or stack[-1] == block:
                destination = i
                break
        else:
            # If no suitable stack found, create a new one
            destination = len(sorted_stacks)
            sorted_stacks.append([])
        # Add the block to the destination stack
        sorted_stacks[destination].append(block)
        # Update the costs
        heapq.heappush(queue, (cost + costs[destination], destination))
        # Add the transfer pair to the result
        transfers.append((index, destination))

    return transfers

stacks = [[], ['Yellow', 'Red', 'Black', 'Yellow', 'Green'], [], [], 
          ['Green', 'Red', 'Blue', 'Blue', 'Black'], 
          ['Green', 'Blue', 'Yellow', 'Red', 'Yellow'], [], 
          ['Blue', 'Green', 'Black', 'Red', 'Black']]

costs = [5, 5, 5, 6, 5, 5, 9, 6]

print(restricted_sorting(stacks, costs))
