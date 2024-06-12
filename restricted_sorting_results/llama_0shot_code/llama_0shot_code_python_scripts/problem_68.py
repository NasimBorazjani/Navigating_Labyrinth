
import heapq

def restricted_sorting(stacks, costs):
    # Convert the given lists into a more manageable data structure
    color_dict = {}
    for i, stack in enumerate(stacks):
        for color in stack:
            if color not in color_dict:
                color_dict[color] = []
            color_dict[color].append(i)

    # Sort the stacks for each color based on the costs
    for color in color_dict:
        color_dict[color] = sorted(color_dict[color], key=lambda x: costs[x])

    # Move the blocks
    transfer_pairs = []
    total_cost = 0
    for color in color_dict:
        while len(color_dict[color]) > 1:
            from_stack = color_dict[color].pop()
            to_stack = color_dict[color][0]
            total_cost += costs[from_stack] - costs[to_stack]
            transfer_pairs.append((from_stack, to_stack))
            heapq.heapify(color_dict[color])

    return transfer_pairs, total_cost

stacks = [['Black', 'Black', 'White', 'Blue', 'Yellow', 'White'], 
          ['Black', 'Blue', 'Red', 'Blue', 'Red', 'Green'], 
          [], 
          ['Black', 'White', 'Red', 'Green', 'White', 'Blue'], 
          ['Yellow', 'Blue', 'Red', 'Green', 'Green', 'Yellow'], 
          [], 
          ['Green', 'Black', 'Red', 'White', 'Yellow', 'Yellow'], 
          [], 
          [], 
          []]

costs = [9, 11, 2, 10, 8, 6, 4, 4, 7, 3]

transfer_pairs, total_cost = restricted_sorting(stacks, costs)
print(transfer_pairs)
print(total_cost)
