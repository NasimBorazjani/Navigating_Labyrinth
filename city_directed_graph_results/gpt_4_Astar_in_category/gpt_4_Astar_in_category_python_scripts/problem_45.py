
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
    ]

    # Define the names of the cities
    city_names = ['Z', 'H', 'M', 'P', 'B', 'I', 'E', 'L', 'Q', 'Y', 'V', 'C']

    # Define the initial state and the goal state
    initial_state = ('C', False, False, False, False)
    goal_state = ('C', True, True, True, True)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, ['C'], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, path, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state == goal_state:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the neighboring cities
        for i in range(len(city_names)):
            # Check if there is a road from the current city to the city at index i
            if adjacency_matrix[city_names.index(state[0])][i] == 1:
                # Generate the new state
                new_state = list(state)
                new_state[0] = city_names[i]
                # If the new city is M or Q and it has not been visited twice yet, increment the corresponding visited counter
                if city_names[i] == 'M' and new_state[1] < 2:
                    new_state[1] += 1
                elif city_names[i] == 'Q' and new_state[2] < 2:
                    new_state[2] += 1
                # If the new city is not M or Q and it has not been visited yet, set the corresponding visited flag to True
                elif city_names[i] != 'M' and city_names[i] != 'Q' and not new_state[3]:
                    new_state[3] = True
                # If the new city has already been visited, skip this action
                elif city_names[i] in path and city_names[i] != 'M' and city_names[i] != 'Q':
                    continue
                new_state = tuple(new_state)

                # The cost so far is the number of actions taken, as the task is to minimize the number of actions required
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, path + [new_state[0]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of cities that have not been visited yet
    # This heuristic is admissible because it never overestimates the cost to reach the goal, as each unvisited city must be visited at least once
    # This heuristic is consistent because the cost of moving from one city to another is always 1, which is exactly the decrease in the number of unvisited cities, if the city is moved toward its goal position
    return sum(1 for i in range(1, len(state)) if state[i] < goal[i])

print(a_star())
