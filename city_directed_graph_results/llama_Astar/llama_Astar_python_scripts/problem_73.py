
import heapq


def a_star():
   # Define the adjacency matrix and the start city
   adjacency_matrix = [
       [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
       [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
       [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
       [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
       [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
       [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
       [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
       [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
   ]
   start = 'Y'
  
   # Define the cities to visit exactly twice
   destinations = ['K', 'S']
  
   # Define the list of cities
   cities = ['K', 'N', 'S', 'Y', 'O', 'I', 'T', 'D', 'M', 'Z', 'R', 'B', 'E', 'F']
  
   # Initialize the visited costs and the queue
   visited_costs = {(start, 0): 0}
   queue = [(0, 0, [], start)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, (city, visits) = heapq.heappop(queue)


       # Check if the current state is the goal state
       if city in destinations and visits == 2:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for i, row in enumerate(adjacency_matrix):
           if row[cities.index(city)] == 1:
               # The new city is the city of the current column
               new_city = cities[i]
               # The new visits is the current visits plus 1 if the new city is a destination city, else remains the same
               new_visits = visits + 1 if new_city in destinations else visits
               # The new state is the new city and the new visits
               new_state = (new_city, new_visits)
               # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the straight-line distance between the current city and the destination cities, as the task is to minimize the total travel time
                   h = heuristic(city, new_city, destinations)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_city], new_state))
   return None


def heuristic(city, new_city, destinations):
   # The heuristic is the straight-line distance between the current city and the destination cities
   # The distance is calculated as the number of cities between the current city and the destination cities, as the cities are directly connected
   h = sum(1 for dest in destinations if abs(cities.index(city) - cities.index(dest)) < abs(cities.index(new_city) - cities.index(dest)))
   return h


print(a_star())
