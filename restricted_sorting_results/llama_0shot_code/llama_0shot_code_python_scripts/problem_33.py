
import heapq

def restricted_sorting(stacks, costs):
    # Create a list of stacks with their initial state and costs
    stacks = [{'shades': list(reversed(shades)), 'cost': costs[i]} for i, shades in enumerate(stacks)]
    
    # Create a priority queue with all the stacks
    queue = [(-stack['shades'][0], i) if stack['shades'] else (float('inf'), i) for i, stack in enumerate(stacks)]
    heapq.heapify(queue)
    
    transfers = []
    
    while True:
        # Get the stack with the least shade (or 'infinity' if it's empty)
        shade, src = heapq.heappop(queue)
        if shade == float('inf'):
            break
        shade = -shade
        
        # Find the best destination stack for the block
        dest = None
        for _ in range(len(stacks)):
            _shade, dst = heapq.heappop(queue)
            if _shade == float('inf'):
                if dest is None:
                    dest = dst
            elif len(stacks[dst]['shades']) < 4 or stacks[dst]['shades'][-1] == shade:
                if dest is None or stacks[dst]['cost'] < stacks[dest]['cost']:
                    dest = dst
            else:
                heapq.heappush(queue, (stacks[dst]['shades'][0], dst))
        
        # Move the block to the destination stack
        heapq.heappush(queue, (stacks[src]['shades'].pop(), src))
        if dest is not None:
            stacks[dest]['shades'].append(shade)
            heapq.heappush(queue, (stacks[dest]['shades'][0], dest))
        else:
            heapq.heappush(queue, (float('inf'), src))
        
        # Add the transfer to the list
        transfers.append((src, dest))
    
    return transfers

stacks = [['Black', 'Yellow', 'Green', 'Red', 'Black'], [], ['Red', 'Yellow', 'Green', 'Blue', 'Green'], [], ['Blue', 'Red', 'Blue', 'Green', 'Yellow'], ['Red', 'Blue', 'Yellow', 'Black', 'Black'], [], []]
costs = [1, 6, 6, 2, 9, 2, 9, 6]

print(restricted_sorting(stacks, costs))
