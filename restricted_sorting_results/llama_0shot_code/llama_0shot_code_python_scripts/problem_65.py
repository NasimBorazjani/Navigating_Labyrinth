
import heapq

def restricted_sorting(stacks):
    # Step 1: Initialize the dictionary of block colors
    colors = {}

    # Step 2: Count the number of blocks of each color
    for stack in stacks:
        for block in stack:
            if block not in colors:
                colors[block] = 0
            colors[block] += 1

    # Step 3: Initialize the priority queue and the dictionary of stacks
    queue = []
    for i, stack in enumerate(stacks):
        if stack:
            color = stack[-1]
            cost = stack[0:5].count(color) * 3 + 6
            heapq.heappush(queue, (cost, i, color))
        else:
            heapq.heappush(queue, (0, i, None))

    # Step 4: Start a loop to transfer blocks
    result = []
    while colors:
        cost, from_stack, color = heapq.heappop(queue)
        to_stack = None
        for i, stack in enumerate(stacks):
            if not stack or stack[-1] == color:
                to_stack = i
                break
        if to_stack is not None:
            # Move the block
            result.append((from_stack, to_stack))
            colors[color] -= 1
            if not colors[color]:
                del colors[color]
            if len(stacks[to_stack]) < 5:
                stacks[to_stack].append(color)
                # Update the cost of the from_stack
                if stacks[from_stack]:
                    new_color = stacks[from_stack][-1]
                    new_cost = stacks[from_stack].count(new_color) * 3 + 6
                    heapq.heappush(queue, (new_cost, from_stack, new_color))
                else:
                    heapq.heappush(queue, (0, from_stack, None))
        else:
            # If no suitable stack is found, increase the cost and push the block back to the queue
            heapq.heappush(queue, (cost + 1, from_stack, color))

    # Step 5: Return the result
    return result
