
import heapq


def a_star():
   # Define the initial state of the map, as a 2d tuple
   initial_state = (('L', '0', '0', '0', '1', '0', '1', '0', '1', '0', '0', '1'),
                   ('0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0'),
                   ('1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'),
                   ('0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0'),
                   ('0', '1', '0', '0', '0', '0', '1', '0', '1', '0', '0', '1'),
                   ('1', '0', '0', '1', '1', '0', '1', '0', '1', '0', '0', '0'),
                   ('0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '0', '0'),
                   ('0', '1', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0'),
                   ('0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1'),
                   ('1', '0', '0', '1', '1', '0', '0', '1', '0', '0', '0', '1'),
                   ('0', '1', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0'),
                   ('0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0'))
  
   # Encoding other variables given in the problem statement
   num_cities = 12
   start_city = 'L'
   destination_cities = ['M', 'Q']
   num_visits = 2


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when we have visited the destination cities exactly twice
       if all(state.count(city) == num_visits for city in destination_cities):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the other cities
       for city_ind in range(num_cities):
           city = state[city_ind]
           if city != '0' and city != start_city:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               # The cost of moving to the new city is the same as the cost of moving from the current city
               new_cost = g + int(new_state[city_ind][city_ind])
               # Update the state to reflect the move
               new_state[city_ind][city_ind] = start_city
               new_state[0][city_ind] = city
               new_state = tuple(tuple(row) for row in new_state)


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, destination_cities, num_visits)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [(city, city_ind)], new_state))
   return None


def heuristic(state, destination_cities, num_visits):
   # An admissible and consistent heuristic for this problem is the sum of the minimum number of moves to visit each destination city the remaining number of times
   # This heuristic relaxes the constraint that we can only visit each city once on our path
   # It is admissible because it never overestimates the cost to reach the goal, as each move must be made at least once
   # It's consistent because moving to a city is costlier than staying at the current city, ensuring h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for city in destination_cities:
       remaining_visits = num_visits - state.count(city)
       # The cost of visiting the city is the minimum number of moves to visit the city the remaining number of times
       h += min(int(state[city_ind][city_ind]) for city_ind in range(len(state)) if state[city_ind][city_ind] == city) * remaining_visits
   return h


print(a_star())
