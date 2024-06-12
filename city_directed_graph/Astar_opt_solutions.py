import heapq


def a_star(adjacency_matrix, cities, initial_city, goals):
    # Define the number of cities
    num_cities = len(cities)

    initial_state = (initial_city, 0, 0, (initial_city))
        
    visited_costs = {}
    visited_costs[initial_state] = 0


    queue = [(0, 0, initial_state)]


    while queue:
        _, g, state = heapq.heappop(queue)
        
        current_city, visited_first, visited_second, visited_cities = state


        # If the current state is one of the goal states and the other goal state has been visited, return the path
        if visited_first==2 and visited_second == 2:
            return list(visited_cities)

        for i in range(num_cities):
            if (cities[i] not in visited_cities or 
                (cities[i] == goals[1] and visited_cities.count(goals[1]) < 2) or
                (cities[i] == goals[0] and visited_cities.count(goals[0]) < 2))  and adjacency_matrix[cities.index(current_city)][cities.index(cities[i])] == 1:
                visited_first_new = visited_first + (cities[i] == goals[0])
                visited_second_new = visited_second + (cities[i] == goals[1])
                new_state = (cities[i], visited_first_new, visited_second_new, tuple(list(visited_cities) + [cities[i]])) 
                new_cost = g + 1


                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The new state must be added to the path
                    heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, new_state))
    return None


def heuristic(state):
    h = 0
    if state[1]< 2:
        h += 2 - state[1]
    if state[2] < 2:
        h += 2 - state[2]
    return h

import sys
def main():
    # Read the initial state from the command line
    adjacency_matrix = eval(sys.argv[1])
    cities = eval(sys.argv[2])
    initial_city = eval(sys.argv[3])[0]
    goals = eval(sys.argv[4])
    print(a_star(adjacency_matrix, cities, initial_city, goals))

if __name__ == "__main__":
    main()
