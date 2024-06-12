
import heapq

def a_star():
    # Define the adjacency matrix of the cities
    adjacency_matrix = [[0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                        [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
                        [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                        [1, 0, 0, 1, 0, 0, 1, 0, 0, 0]]

    # Define the names of the cities
    cities = ['R', 'B', 'F', 'Z', 'N', 'H', 'A', 'P', 'M', 'J']

    # Define the initial state and the goal state
    initial_state = ('Z', False, False, False, False, False, False, False, False, False, 0, 0)
    goal_state = ('Z', True, True, False, False, True, False, False, False, False, 2, 2)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, ['Z'], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state, return the actions taken
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving to any of the cities connected to the current city
        for i in range(len(cities)):
            # Check if the new state would be valid, ie if there is a road from the current city to the new city and if the new city has not been visited yet or if it is one of the destination cities and it has been visited less than 2 times
            if adjacency_matrix[cities.index(state[0])][i] == 1 and (state[i+1] == False or (cities[i] in ['B', 'H'] and state[i+1] == True and state[10+(i==1)] < 2)):
                # Generate the new state
                new_state = list(state)
                new_state[0] = cities[i]
                new_state[i+1] = True
                if cities[i] in ['B', 'H']:
                    new_state[10+(i==1)] += 1
                new_state = tuple(new_state)
                # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
                new_cost = g + 1

                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [new_state[0]], new_state))
    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the number of destination cities that have not been visited twice
    # The heuristic relaxes the constraint that we can only move to cities that are directly connected and presumes we can move directly to any of the destination cities
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving from one city to another is always 1, which is exactly the decrease in the heuristic cost, if the city is a destination city and it has not been visited twice, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as all destination cities have been visited twice in the goal state.
    return 2 - state[10] + 2 - state[11]

print(a_star())
