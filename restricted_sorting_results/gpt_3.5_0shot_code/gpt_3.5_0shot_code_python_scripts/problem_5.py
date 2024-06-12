
from itertools import permutations

# Define the initial state of the stacks
stacks = [['Red', 'Green', 'Green', 'Yellow'], [], ['Blue', 'Blue', 'Green', 'Red'], [], ['Blue', 'Yellow', 'Red', 'Yellow'], []]

# Define the cost of moving one block to the top of each stack
cost = {0: 4, 1: 1, 2: 7, 3: 3, 4: 2, 5: 2}

# Function to calculate the cost of a sequence of transfers
def calculate_cost(transfers):
    total_cost = 0
    for transfer in transfers:
        total_cost += cost[transfer[0]]
    return total_cost

# Function to check if a stack is sorted
def is_sorted(stack):
    return all(stack[i] <= stack[i+1] for i in range(len(stack)-1))

# Function to generate all possible transfer sequences
def generate_transfers():
    transfer_permutations = permutations(range(6), 2)
    return list(transfer_permutations)

# Function to apply a sequence of transfers to the stacks
def apply_transfers(transfers):
    for transfer in transfers:
        if stacks[transfer[0]] and (not stacks[transfer[1]] or stacks[transfer[0]][-1] == stacks[transfer[1]][-1]):
            stacks[transfer[1]].append(stacks[transfer[0]].pop())
    return stacks

# Find the sequence of transfers with the least cost that results in all blocks being correctly sorted
min_cost = float('inf')
best_transfers = None

for transfers in generate_transfers():
    temp_stacks = [stack.copy() for stack in stacks]
    apply_transfers([transfers])
    
    if all(is_sorted(stack) for stack in stacks):
        current_cost = calculate_cost([transfers])
        if current_cost < min_cost:
            min_cost = current_cost
            best_transfers = [transfers]

# Print the list of transfer pairs with the least possible cost
print(best_transfers)
