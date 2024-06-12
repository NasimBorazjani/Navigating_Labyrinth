
import heapq

def restricted_sorting(stacks, costs):
    moves = []
    colors = ['Yellow', 'Pink', 'Black', 'Green', 'White', 'Blue', 'Red']
    color_to_stack = {color: i for i, color in enumerate(colors)}
    heap = [(0, stacks, [])]

    while heap:
        cost, stacks, path = heapq.heappop(heap)
        if is_goal(stacks):
            return path
        for move in get_moves(stacks, costs):
            new_stacks = apply_move(stacks, move)
            new_cost = cost + costs[move[1]]
            new_path = path + [move]
            heapq.heappush(heap, (new_cost, new_stacks, new_path))

def is_goal(stacks):
    for stack in stacks:
        if len(stack) > 1 and len(set(stack)) > 1:
            return False
    return True

def get_moves(stacks, costs):
    moves = []
    for i, stack in enumerate(stacks):
        if stack:
            for j, cost in enumerate(costs):
                if i != j and (not stacks[j] or stacks[j][-1] == stack[-1]):
                    moves.append((i, j))
    return moves

def apply_move(stacks, move):
    new_stacks = [list(stack) for stack in stacks]
    block = new_stacks[move[0]].pop()
    new_stacks[move[1]].append(block)
    return new_stacks

stacks = [['Yellow', 'Yellow', 'Pink', 'Black', 'Green', 'Green', 'Yellow'], ['Pink', 'Yellow', 'White', 'Red', 'Black', 'Blue', 'Blue'], [], [], ['Pink', 'Green', 'Pink', 'Pink', 'Blue', 'Red', 'Red'], ['Black', 'Black', 'Black', 'Blue', 'Yellow', 'Red', 'White'], [], [], [], [], ['Green', 'Blue', 'Red', 'Red', 'Green', 'White', 'Black'], ['White', 'White', 'Green', 'Yellow', 'Blue', 'White', 'Pink']]
costs = {0: 12, 1: 11, 2: 5, 3: 11, 4: 10, 5: 9, 6: 5, 7: 5, 8: 3, 9: 10, 10: 5, 11: 5}

print(restricted_sorting(stacks, costs))
