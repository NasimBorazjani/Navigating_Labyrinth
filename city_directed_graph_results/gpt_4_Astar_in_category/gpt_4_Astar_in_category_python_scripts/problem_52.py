
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    city_map = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
                [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
                [0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0]]

    # Define the city names
    city_names = ['C', 'L', 'D', 'O', 'A', 'Z', 'M', 'H', 'K', 'R', 'Q', 'N', 'J']

    # Define the initial state and goal state
    initial_state = (2, 0, 0, [False]*13, [2])  # (current city, number of visits to D, number of visits to J, visited cities, path)
    goal_state = (2, 2, 2)  # (current city, number of visits to D, number of visits to J)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element
    queue = [(0, 0, initial_state)]  # (priority, cost so far, state)

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, state = heapq.heappop(queue)

        # If the current state is the goal state, return the path
        if state[:3] == goal_state:
            return [city_names[i] for i in state[4]]

        # Generate all possible actions from the current state, which includes moving to any of the connected cities
        for i in range(13):
            if city_map[state[0]][i] == 1 and (not state[3][i] or i in [2, 12]):  # If there is a road to the city and the city is either not visited or is D or J
                # Generate the new state
                new_state = list(state)
                new_state[0] = i
                new_state[3] = list(state[3])
                new_state[3][i] = True
                new_state[4] = list(state[4])
                new_state[4].append(i)
                if i == 2:  # If the city is D
                    new_state[1] += 1
                elif i == 12:  # If the city is J
                    new_state[2] += 1
                new_state = tuple(new_state)

                # The cost so far is the number of cities visited, as the travel time between any two directly connected cities is the same
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of visits remaining to D and J
    # The heuristic is admissible because it never overestimates the cost to reach the goal, as each remaining visit must be made at least once
    # The heuristic is consistent because the cost of moving from one city to an adjacent city is always 1, which is exactly the decrease in the heuristic if the city is D or J
    return 2 - state[1] + 2 - state[2]

print(a_star())
