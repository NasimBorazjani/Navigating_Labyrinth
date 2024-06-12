
import heapq

def restricted_sorting(stacks, costs):
    # Create a list of stacks with their initial state and costs
    stacks = [{'shades': shades, 'cost': costs[i]} for i, shades in enumerate(stacks)]
    # Initialize the transfer list
    transfers = []
    # While there are still blocks to be sorted
    while any(stack['shades'] for stack in stacks):
        # For each stack
        for i, stack in enumerate(stacks):
            # If the stack is not empty
            if stack['shades']:
                shade = stack['shades'].pop()
                # Find the best destination stack for the block
                dest_stack = min([(cost, j) for j, other in enumerate(stacks) if j != i and (not other['shades'] or other['shades'][-1] == shade) and len(other['shades']) < 4], default=(float('inf'), None), key=lambda x: x[0]*stack['cost'])
                if dest_stack[1] is not None:
                    # Move the block to the destination stack
                    stacks[dest_stack[1]]['shades'].append(shade)
                    transfers.append((i, dest_stack[1]))
    # Return the transfer list
    return transfers

stacks = [[], [], ['Green', 'Yellow', 'Black', 'Red', 'Black'], ['Black', 'Red', 'Yellow', 'Blue', 'Yellow'], ['Green', 'Blue', 'Blue', 'Red', 'Black'], [], [], ['Red', 'Green', 'Blue', 'Green', 'Yellow']]
costs = [5, 5, 1, 7, 7, 9, 1, 6]
print(restricted_sorting(stacks, costs))
