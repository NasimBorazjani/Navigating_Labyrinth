
import heapq

def restricted_sorting(stacks, costs):
    # Initialize priority queue with costs
    queue = [(cost, i) for i, cost in enumerate(costs)]
    heapq.heapify(queue)

    # Initialize result list
    result = []

    # Iterate over stacks
    for i, stack in enumerate(stacks):
        # While stack is not empty
        while stack:
            # Pop block from stack
            block = stack.pop()

            # Find minimum cost stack to move block to
            cost, j = heapq.heappop(queue)

            # Add transfer pair to result
            result.append((i, j))

            # Update priority queue and stacks
            if stack:
                heapq.heappush(queue, (cost + 1, i))
            else:
                heapq.heappush(queue, (cost, i))

    return result

# Initial state of stacks
stacks = [[], [], ['Blue', 'Blue', 'Blue', 'Green', 'Black', 'Red'], [], 
          ['Red', 'Black', 'Blue', 'White', 'Blue', 'Yellow'], 
          ['Yellow', 'White', 'Green', 'Black', 'Yellow', 'Red'], [], [], 
          ['White', 'Black', 'White', 'White', 'Black', 'Red'], 
          ['Red', 'Green', 'Green', 'Yellow', 'Yellow', 'Green']]

# Costs of moving a block to the top of each stack
costs = [3, 10, 9, 8, 8, 7, 6, 9, 2, 8]

print(restricted_sorting(stacks, costs))
