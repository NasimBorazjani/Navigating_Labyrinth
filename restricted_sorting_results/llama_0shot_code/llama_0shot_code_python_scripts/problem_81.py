
import heapq

def restricted_sorting(stacks, costs):
    # Initialize a priority queue with the costs of moving a block to each stack
    queue = [(-cost, i) for i, cost in enumerate(costs)]
    # Initialize a list to keep track of the number of blocks in each stack
    num_blocks = [len(stack) if stack else 0 for stack in stacks]
    # Initialize a list to keep track of the color of the top block in each stack
    top_blocks = [stack[-1] if stack else None for stack in stacks]
    transfers = []
    total_cost = 0

    def move_block(from_stack, to_stack):
        nonlocal total_cost
        total_cost += costs[to_stack]
        transfers.append((from_stack, to_stack))
        num_blocks[from_stack] -= 1
        num_blocks[to_stack] += 1
        heapq.heapify(queue)

    while True:
        # Find a stack to move a block from
        from_stack = num_blocks.index(max(num_blocks))
        if num_blocks[from_stack] == 0:
            break
        # Find the color of the top block in the 'from_stack'
        color = top_blocks[from_stack]
        # Find a stack to move the block to
        while queue:
            cost, to_stack = heapq.heappop(queue)
            if num_blocks[to_stack] < 6 and (top_blocks[to_stack] is None or top_blocks[to_stack] == color):
                move_block(from_stack, to_stack)
                break
        else:
            # If we cannot find a stack to move the block to, sort the 'from_stack'
            while num_blocks[from_stack] > 0:
                to_stack = top_blocks.index(color)
                move_block(from_stack, to_stack)
    return transfers, total_cost

stacks = [[], ['White', 'Black', 'Yellow', 'Black', 'Green', 'Blue', 'Pink'], ['Black', 'Red', 'Yellow', 'White', 'Yellow', 'Black', 'Green'], ['Yellow', 'White', 'Green', 'White', 'White', 'Black', 'Blue'], ['Blue', 'Pink', 'Red', 'Pink', 'Green', 'Yellow', 'Black'], ['White', 'Red', 'Pink', 'Blue', 'Blue', 'Pink', 'Green'], [], [], [], ['Red', 'Pink', 'Red', 'Blue', 'Red', 'Green', 'Yellow'], [], []]
costs = [5, 3, 3, 4, 2, 2, 12, 9, 5, 11, 11, 10]

transfers, total_cost = restricted_sorting(stacks, costs)
print(transfers)
print(total_cost)
