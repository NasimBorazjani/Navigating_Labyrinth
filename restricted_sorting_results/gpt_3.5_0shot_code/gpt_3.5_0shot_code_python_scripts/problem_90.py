
import heapq

# Initial state of the stacks
stacks = [['Pink', 'Black', 'Red', 'White', 'White', 'Black', 'Pink'],
          [],
          [],
          ['Green', 'Green', 'Blue', 'White', 'Pink', 'Pink', 'White'],
          [],
          ['Blue', 'Yellow', 'Yellow', 'Black', 'White', 'Green', 'Red'],
          ['Blue', 'Yellow', 'Blue', 'White', 'Green', 'Red', 'Pink'],
          ['Pink', 'Yellow', 'Yellow', 'Green', 'Green', 'Black', 'Blue'],
          [],
          ['Blue', 'Red', 'Red', 'Black', 'Black', 'Red', 'Yellow'],
          [],
          []]

# Cost dictionary for moving blocks
cost_dict = {0: 2, 1: 7, 2: 2, 3: 2, 4: 4, 5: 13, 6: 4, 7: 6, 8: 8, 9: 6, 10: 10, 11: 10}

# Define a function to calculate the cost of moving a block from one stack to another
def move_cost(from_stack, to_stack):
    return cost_dict[to_stack]

# Define a function to check if a state is a goal state
def is_goal_state(stacks):
    return all(len(set(stack)) == 1 for stack in stacks if stack)

# Define a function to generate possible moves from a given state
def generate_moves(stacks):
    moves = []
    for i, from_stack in enumerate(stacks):
        if not from_stack:
            continue
        for j, to_stack in enumerate(stacks):
            if i == j or (to_stack and to_stack[-1] != from_stack[-1]):
                continue
            moves.append((i, j))
    return moves

# Define a function to calculate the total cost of a state
def total_cost(state):
    return sum(move_cost(move[0], move[1]) for move in state)

# A* search algorithm
def astar_search(stacks):
    heap = [(total_cost([]), [], stacks)]
    while heap:
        _, moves, state = heapq.heappop(heap)
        if is_goal_state(state):
            return moves
        for move in generate_moves(state):
            new_state = [stack.copy() for stack in state]
            new_state[move[1]].append(new_state[move[0]].pop())
            new_moves = moves + [move]
            heapq.heappush(heap, (total_cost(new_moves), new_moves, new_state))

# Solve the problem
solution = astar_search(stacks)
print(solution)
