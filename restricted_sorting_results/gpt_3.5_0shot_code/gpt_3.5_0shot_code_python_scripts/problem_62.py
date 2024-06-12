
from itertools import permutations

# Initial state of the stacks
stacks = [[], [], ['Blue', 'Yellow', 'Red', 'Black', 'White', 'Blue'], ['Blue', 'Green', 'Yellow', 'Red', 'Red', 'White'], [], ['Red', 'Black', 'White', 'Yellow', 'White', 'Green'], [], ['Black', 'Yellow', 'Green', 'Black', 'Black', 'Blue'], [], ['Red', 'Green', 'Green', 'Blue', 'Yellow', 'White']]

# Cost of moving one block to the top of each stack
cost = {0: 6, 1: 10, 2: 8, 3: 3, 4: 5, 5: 7, 6: 10, 7: 6, 8: 3, 9: 8}

# Calculate the cost of a given transfer sequence
def calculate_cost(transfers):
    total_cost = 0
    for transfer in transfers:
        total_cost += cost[transfer[0]]
    return total_cost

# Generate all possible transfer sequences
transfer_sequences = permutations(range(10), 2)

# Find the transfer sequence with the least cost
min_cost = float('inf')
min_transfer_sequence = None
for transfer_sequence in transfer_sequences:
    temp_stacks = [stack.copy() for stack in stacks]
    transfers = []
    for transfer in transfer_sequence:
        if temp_stacks[transfer[0]] and (not temp_stacks[transfer[1]] or temp_stacks[transfer[0]][-1] == temp_stacks[transfer[1]][-1]):
            temp_stacks[transfer[1]].append(temp_stacks[transfer[0]].pop())
            transfers.append(transfer)
    if all(len(stack) == 0 or len(set(stack)) == 1 for stack in temp_stacks):
        current_cost = calculate_cost(transfers)
        if current_cost < min_cost:
            min_cost = current_cost
            min_transfer_sequence = transfers

# Print the transfer sequence with the least cost
print(min_transfer_sequence)
