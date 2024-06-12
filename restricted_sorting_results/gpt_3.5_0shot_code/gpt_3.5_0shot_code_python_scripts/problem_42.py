
from itertools import permutations

# Initial state of the stacks
stacks = [['Blue', 'Black', 'Yellow', 'Black', 'Red'],
          ['Blue', 'Blue', 'Green', 'Black', 'Yellow'],
          [],
          ['Yellow', 'Red', 'Red', 'Green', 'Green'],
          [],
          [],
          ['Red', 'Blue', 'Black', 'Green', 'Yellow'],
          []]

# Cost of moving one block to the top of each stack
cost = {0: 7, 1: 5, 2: 7, 3: 2, 4: 6, 5: 7, 6: 5, 7: 3}

# Function to calculate the total cost of a sequence of transfers
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
    min_cost = float('inf')
    min_transfers = None

    for perm in permutations(range(8)):
        transfers = []
        for i in range(5):
            for j in range(8):
                if stacks[j] and (not stacks[perm[i]] or stacks[j][-1] == stacks[perm[i]][-1]):
                    transfers.append((j, perm[i]))
                    stacks[perm[i]].append(stacks[j].pop())
        
        if all(is_sorted(stack) for stack in stacks) and calculate_cost(transfers) < min_cost:
            min_cost = calculate_cost(transfers)
            min_transfers = transfers

        # Reset stacks for next permutation
        stacks[:] = [['Blue', 'Black', 'Yellow', 'Black', 'Red'],
                     ['Blue', 'Blue', 'Green', 'Black', 'Yellow'],
                     [],
                     ['Yellow', 'Red', 'Red', 'Green', 'Green'],
                     [],
                     [],
                     ['Red', 'Blue', 'Black', 'Green', 'Yellow'],
                     []]

    return min_transfers

# Get the list of transfer pairs with the least possible cost
result = generate_transfers()
print(result)
