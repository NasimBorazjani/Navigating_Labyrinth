
import heapq


def a_star():
   # Define the initial state of the map, as a 2d tuple
   initial_state = (('G', 'S', 'S', 'E', 'E', 'B', 'P', 'Q', 'D', 'N', 'J', 'R', 'W'),
                   ('R', 'S', 'W', 'B', 'P', 'G', 'Q', 'E', 'N', 'D', 'J', 'S', 'E'))
   # Define the start city and the destination cities
   start = 'G'
   destinations = ['S', 'E']
   num_cities = 12


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when we have visited the destination cities exactly twice
       if all(state[0].count(destination) == 2 for destination in destinations):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the other cities
       for city in range(num_cities):
           # Check if the new state would be valid, ie the city must not be the start city or any of the destination cities
           if state[0][city] != start and state[0][city] not in destinations:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               # Move to the new city
               new_state[0][city] = start
               new_state[1][city] = state[0][city]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, destinations), new_cost, actions + [state[0][city]], new_state))
   return None


def heuristic(state, destinations):
   # An admissible and consistent heuristic for this problem is the sum of the distances from the current city to the destination cities
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as the cost of moving from any city to any other city is the same
   # It's consistent because moving to any city increases the heuristic cost of the successor node by a max of 1 (if the moved city is a destination city), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for city in state[0]:
       if city not in destinations:
           h += min(abs(city_ind - state[0].index(destination)) for destination in destinations)
   return h


print(a_star())
