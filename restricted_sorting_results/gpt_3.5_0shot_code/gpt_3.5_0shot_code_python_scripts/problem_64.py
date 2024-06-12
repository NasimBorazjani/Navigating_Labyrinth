
from itertools import permutations

# Initial state of the stacks
stacks = [['White', 'White', 'Yellow', 'White', 'White', 'Black'], [], ['Red', 'Red', 'Green', 'Green', 'Green', 'Red'], ['Black', 'Yellow', 'Black', 'Yellow', 'Blue', 'Green'], ['Yellow', 'Blue', 'Black', 'Green', 'Blue', 'Red'], [], ['Red', 'Black', 'Blue', 'Yellow', 'Blue', 'White'], [], [], []]

# Cost of moving one block to the top of each stack
cost = {0: 6, 1: 7, 2: 11, 3: 10, 4: 7, 5: 2, 6: 3, 7: 3, 8: 11, 9: 8}

# Function to calculate the cost of a given transfer sequence
def calculate_cost(transfers):
    total_cost = 0
    for transfer in transfers:
        total_cost += cost[transfer[0]]
    return total_cost

# Function to check if a stack is sorted
def is_sorted(stack):
    return all(block == stack[0] for block in stack)

# Function to generate all possible transfer sequences
def generate_transfers():
    transfer_permutations = permutations(range(10), 2)
    return list(transfer_permutations)

# Function to apply a transfer to the stacks
def apply_transfer(transfers, stacks):
    new_stacks = [stack.copy() for stack in stacks]
    for transfer in transfers:
        block = new_stacks[transfer[0]].pop()
        new_stacks[transfer[1]].append(block)
    return new_stacks

# Function to find the optimal transfer sequence
def find_optimal_transfers(stacks):
    optimal_transfers = None
    min_cost = float('inf')
    transfer_sequences = generate_transfers()
    
    for transfers in transfer_sequences:
        new_stacks = apply_transfer(transfers, stacks)
        if all(is_sorted(stack) for stack in new_stacks):
            current_cost = calculate_cost(transfers)
            if current_cost < min_cost:
                min_cost = current_cost
                optimal_transfers = transfers
    
    return optimal_transfers

# Find the optimal transfer sequence
optimal_transfers = find_optimal_transfers(stacks)
print([(transfer[0], transfer[1]) for transfer in optimal_transfers])
