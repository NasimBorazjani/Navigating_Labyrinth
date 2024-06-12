
import heapq


def a_star():
   # Define the adjacency matrix of the map
   adjacency_matrix = [
       [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
       [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
       [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
       [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1]
   ]
   # Define the start city and the destination cities
   start = 'B'
   destinations = ['E', 'N']
   # Define the cities in the map
   cities = 'ANBMZOEQGLPE'
   # Define the goal state as visiting each destination city twice
   goal_state = (2, 2)
   # Define the initial state as starting from the start city and having visited each destination city zero times
   initial_state = (0, 0)
   # Define the number of cities
   num_cities = len(cities)


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the path to reach each state in a list; no path performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving to any directly connected city
       for city_ind in range(num_cities):
           # Check if the new state would be valid, ie the city must be directly connected to the current city and not be a destination city if it has been visited once
           if adjacency_matrix[cities.index(start)][city_ind] == 1 and (cities[city_ind] not in destinations or state[cities.index(destinations[0])] < 2 or state[cities.index(destinations[1])] < 2):
               # Generate the new state
               new_state = list(state)[:]
               new_state[city_ind] += 1
               new_state = tuple(new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal state
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, goal_state, cities, destinations)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [cities[city_ind]], new_state))
   return None


def heuristic(state, goal_state, cities, destinations):
   # An admissible and consistent heuristic for this problem is the sum of the distances from the current state to the goal state
   # This heuristic relaxes the constraint that we can only visit each city once on our path
   # It is admissible because it never overestimates the cost to reach the goal, as each overestimated distance must be visited at least once
   # It's consistent because moving to a city reduces the heuristic cost of the successor node by a max of 1 (if the moved city is a destination city and has been visited once), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state)):
       if cities[i] in destinations:
           h += abs(state[i] - goal_state[cities.index(destinations[0])]) + abs(state[i] - goal_state[cities.index(destinations[1])])
   return h


print(a_star())
