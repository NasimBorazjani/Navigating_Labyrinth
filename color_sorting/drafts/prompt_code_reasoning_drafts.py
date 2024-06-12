from collections import deque

def bfs():
    tubes = [['Green', 'Red', 'Green', 'Red'], ['Blue', 'Blue', 'Red', 'Green'], ['Red', 'Blue', 'Green', 'Blue']]
    num_tubes = 3
    capacity = 6
    """tubes = [['Pink', 'Orange', 'White', 'Teal', 'Gray', 'Purple', 'Gray', 'Brown', 'Orange', 'Red', 'Purple', 'Yellow', 'Blue'], ['White', 'Blue', 'Red', 'Black', 'Brown', 'Teal', 'Gray', 'Orange', 'Blue', 'Red', 'Green', 'Purple', 'Red'], ['Black', 'Orange', 'Brown', 'Black', 'Pink', 'White', 'Orange', 'Pink', 'Pink', 'Yellow', 'Yellow', 'Yellow', 'Pink'], ['Green', 'Black', 'Red', 'Purple', 'White', 'Black', 'Orange', 'Blue', 'Green', 'Gray', 'Purple', 'Red', 'Green'], ['Teal', 'Black', 'Purple', 'Teal', 'Brown', 'Brown', 'Brown', 'Green', 'Blue', 'Blue', 'Gray', 'Teal', 'Orange'], ['Yellow', 'Blue', 'Teal', 'Yellow', 'Yellow', 'Purple', 'Orange', 'Red', 'Purple', 'Purple', 'Pink', 'White', 'Gray'], ['Black', 'Green', 'Brown', 'Pink', 'Black', 'White', 'Teal', 'Orange', 'Teal', 'Pink', 'Teal', 'White', 'Purple'], ['Teal', 'Red', 'Pink', 'Gray', 'Black', 'Green', 'Yellow', 'Brown', 'White', 'Gray', 'Black', 'Green', 'Blue'], ['Brown', 'White', 'Pink', 'Yellow', 'Brown', 'Purple', 'Purple', 'Brown', 'Purple', 'Brown', 'White', 'Gray', 'Orange'], ['Orange', 'Red', 'Yellow', 'Orange', 'White', 'Blue', 'Red', 'Green', 'Blue', 'Yellow', 'Blue', 'Red', 'White'], ['Gray', 'Black', 'Teal', 'Green', 'Gray', 'Pink', 'Pink', 'Gray', 'White', 'Black', 'Blue', 'Teal', 'Green'], ['Orange', 'Yellow', 'Red', 'Green', 'Teal', 'Brown', 'Blue', 'Green', 'Black', 'Red', 'Pink', 'Gray', 'Yellow']]
    num_tubes = 12
    capacity = 15"""
    # Initialize a set to keep track of visited states
    visited = set()
    # Initialize a queue to keep track of the states to be explored with the initial state and an empty list of actions.
    queue = deque([(tubes, [])])

    while queue:
        state, actions = queue.popleft()
        # Check if the state is the goal state
        if all(len(set(tube)) <= 1 for tube in state):
            return actions
        # For each state, generate all possible actions, which includes moving a ball from one tube to another
        for from_tube_ind in range(num_tubes):
            for to_tube_ind in range(num_tubes):
                if from_tube_ind != to_tube_ind and state[from_tube_ind] and len(state[to_tube_ind]) < capacity:
                    # Generate the new state
                    new_state = [list(tube[:]) for tube in state]
                    ball_to_move = new_state[from_tube_ind].pop(0)
                    new_state[to_tube_ind].insert(0, ball_to_move)
                    new_state = tuple(tuple(tube) for tube in new_state)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, actions + [(from_tube_ind, to_tube_ind)]))
    return None

"""import time

start_time = time.time()

print(bfs())

end_time = time.time()

execution_time = end_time - start_time
print(f"The execution time of bfs is {execution_time} seconds")"""



import heapq
from collections import Counter


"""def heuristic(tubes):
    # The heuristic function is the number of balls that are not the same color as the most frequent color in their tube
    h = 0
    for tube in tubes:
        if tube:
            most_common_color = Counter(tube).most_common(1)[0][0]
            for ball in tube:
                if ball != most_common_color:
                    h += 1
    print(tubes, h)
    return h"""


def heuristic(tubes):
    h = 0
    most_common_colors = []
    for tube in tubes:
        if tube:
            color_counts = Counter(tube)
            most_common_list = color_counts.most_common()
            most_common_color = None
            i = 0
            # Keep checking the next most common color until we find one that hasn't been chosen yet
            while i < len(most_common_list) and most_common_list[i][0] in most_common_colors:
                i += 1
            if i < len(most_common_list):
                most_common_color = most_common_list[i][0]
                most_common_colors.append(most_common_color)
            for ball in tube:
                if ball != most_common_color:
                    h += 1
    #print(tubes, h)
    return h

def a_star():
    tubes = [['Green', 'Red', 'Green', 'Red'], ['Blue', 'Blue', 'Red', 'Green'], ['Red', 'Blue', 'Green', 'Blue']]
    num_tubes = 3
    capacity = 6
    """tubes = [['Pink', 'Orange', 'White', 'Teal', 'Gray', 'Purple', 'Gray', 'Brown', 'Orange', 'Red', 'Purple', 'Yellow', 'Blue'], ['White', 'Blue', 'Red', 'Black', 'Brown', 'Teal', 'Gray', 'Orange', 'Blue', 'Red', 'Green', 'Purple', 'Red'], ['Black', 'Orange', 'Brown', 'Black', 'Pink', 'White', 'Orange', 'Pink', 'Pink', 'Yellow', 'Yellow', 'Yellow', 'Pink'], ['Green', 'Black', 'Red', 'Purple', 'White', 'Black', 'Orange', 'Blue', 'Green', 'Gray', 'Purple', 'Red', 'Green'], ['Teal', 'Black', 'Purple', 'Teal', 'Brown', 'Brown', 'Brown', 'Green', 'Blue', 'Blue', 'Gray', 'Teal', 'Orange'], ['Yellow', 'Blue', 'Teal', 'Yellow', 'Yellow', 'Purple', 'Orange', 'Red', 'Purple', 'Purple', 'Pink', 'White', 'Gray'], ['Black', 'Green', 'Brown', 'Pink', 'Black', 'White', 'Teal', 'Orange', 'Teal', 'Pink', 'Teal', 'White', 'Purple'], ['Teal', 'Red', 'Pink', 'Gray', 'Black', 'Green', 'Yellow', 'Brown', 'White', 'Gray', 'Black', 'Green', 'Blue'], ['Brown', 'White', 'Pink', 'Yellow', 'Brown', 'Purple', 'Purple', 'Brown', 'Purple', 'Brown', 'White', 'Gray', 'Orange'], ['Orange', 'Red', 'Yellow', 'Orange', 'White', 'Blue', 'Red', 'Green', 'Blue', 'Yellow', 'Blue', 'Red', 'White'], ['Gray', 'Black', 'Teal', 'Green', 'Gray', 'Pink', 'Pink', 'Gray', 'White', 'Black', 'Blue', 'Teal', 'Green'], ['Orange', 'Yellow', 'Red', 'Green', 'Teal', 'Brown', 'Blue', 'Green', 'Black', 'Red', 'Pink', 'Gray', 'Yellow']]
    num_tubes = 12
    capacity = 15"""
    tubes = [['Blue', 'Green', 'Pink', 'Yellow', 'Pink', 'Green', 'Red', 'White', 'Black', 'Blue', 'Blue', 'Pink'], ['Yellow', 'Red', 'Pink', 'Blue', 'Green', 'Pink', 'Red', 'Yellow', 'Yellow', 'Black', 'White', 'Black'], ['Blue', 'Pink', 'Yellow', 'Pink', 'White', 'Black', 'Red', 'Blue', 'Black', 'White', 'White', 'White'], ['White', 'Yellow', 'White', 'Green', 'Green', 'Red', 'Black', 'Green', 'Blue', 'Black', 'Black', 'Blue'], ['Pink', 'Blue', 'Green', 'Yellow', 'Yellow', 'Red', 'Red', 'Green', 'Yellow', 'Red', 'Black', 'Red'], ['Red', 'Blue', 'Pink', 'Black', 'White', 'Red', 'Black', 'Blue', 'Pink', 'Black', 'White', 'Pink'], ['White', 'Red', 'Blue', 'Green', 'Green', 'Green', 'Pink', 'Green', 'White', 'Yellow', 'Yellow', 'Yellow']]
    num_tubes = 7
    capacity = 15
    # Initialize a set to keep track of visited states
    visited_costs = {}
    # Initialize a priority queue to keep track of the states to be explored with the initial state and an empty list of actions.
    # The priority of a state is the total cost, which is the number of moves made so far (g(n)) plus the heuristic value of the state (h(n)).
    queue = [(heuristic(tubes), 0, tubes, [])]

    while queue:
        _, g, state, actions = heapq.heappop(queue)
        # Check if the state is the goal state
        if all(len(set(tube)) <= 1 for tube in state):
            return actions
        # For each state, generate all possible actions, which includes moving a ball from one tube to another
        for from_tube_ind in range(num_tubes):
            for to_tube_ind in range(num_tubes):
                if from_tube_ind != to_tube_ind and state[from_tube_ind] and len(state[to_tube_ind]) < capacity:
                    # Generate the new state
                    new_state = [list(tube[:]) for tube in state]
                    ball_to_move = new_state[from_tube_ind].pop(0)
                    new_state[to_tube_ind].insert(0, ball_to_move)
                    new_state = tuple(tuple(tube) for tube in new_state)
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        # Add the new state to the queue with the total cost (g + h) as the priority
                        heapq.heappush(queue, (g + heuristic(new_state), g + 1, new_state, actions + [(from_tube_ind, to_tube_ind)]))
    return None
    
    
"""from heapq import heappush, heappop

def a_star():
    tubes = [['Green', 'Red', 'Green', 'Red'], ['Blue', 'Blue', 'Red', 'Green'], ['Red', 'Blue', 'Green', 'Blue']]
    goal = [['Blue', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Red', 'Red']]
    num_tubes = 3
    # Initialize a dict to keep track of the visited states and their costs
    visited_costs = {}
    visited_costs[tuple(map(tuple, tubes))] = 0
    # Initialize a priority queue to keep track of the states to be explored with the initial state and an empty list of actions.
    queue = []
    heappush(queue, (0, 0, (tubes, [])))

    while queue:
        _, g, (state, actions) = heappop(queue)
        if state == tuple(map(tuple, goal)):
            return actions
        # For each state, generate all possible actions, which includes moving a ball from any of the 3 tubes to any of the other 2 tubes
        for from_tube in range(num_tubes):
            for to_tube in range(num_tubes):
                if from_tube != to_tube and state[from_tube] and (not state[to_tube] or len(state[to_tube]) < 6):
                    # Move action. Check if the resulting state is valid
                    # If the tube from which a ball is taken is not empty and the tube to which a ball is moved is not at capacity
                    new_state = [list(tube) for tube in state]
                    ball = new_state[from_tube].pop(0)
                    new_state[to_tube].insert(0, ball)
                    new_state = tuple(map(tuple, new_state))
                    new_cost = g + 1
                    # If the new state has not been visited before or we found a new more optimal path to the state
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_state, goal)
                        heappush(queue, (g + h, g + 1, (new_state, actions + [(from_tube, to_tube)])))
    return None

def heuristic(state, goal):
    h = 0
    for i in range(len(state)):
        tube = state[i]
        goal_color = goal[i][0]
        for color in tube:
            if color != goal_color:
                h += 1
    return h

"""

    

import time

start_time = time.time()

print(a_star())

end_time = time.time()

execution_time = end_time - start_time
print(f"The execution time of A* is {execution_time} seconds")
