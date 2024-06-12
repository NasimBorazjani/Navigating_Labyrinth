
import heapq

def initialize():
    initial_state = (('x', '7', '7', '12', '7', 'x', '13', '1', '18'), ('9', '18', 'x', '4', '19', '8', 'x', '15', '10'), ('9', 'x', '10', '5', '5', '9', '8', 'x', 'x'), ('14', '4', '19', '9', '14', 'x', 'x', '7', '9'), ('9', '4', '11', '15', '7', 'x', '17', '3', 'x'), ('11', 'x', '2', '18', '15', '15', 'x', 'x', 'x'), ('x', '5', '10', 'x', 'x', '13', 'x', '9', 'x'), ('3', 'x', '2', 'x', 'x', 'x', 'x', '4', 'x'), ('x', 'x', '7', 'x', '19', 'x', 'x', 'x', '9'))
    start_workshop = (6, 1)
    end_workshop = (2, 6)
    districts = [(0, 2), (3, 5), (6, 8)]
    moves = [((- 1), 0), (1, 0), (0, (- 1)), (0, 1)]
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [], start_workshop)]
    return (initial_state, start_workshop, end_workshop, districts, moves, visited_costs, queue)

def a_star():
    (initial_state, start_workshop, end_workshop, districts, moves, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, current_workshop) = heapq.heappop(queue)
        if (current_workshop == end_workshop):
            return actions
        for move in moves:
            new_workshop = ((current_workshop[0] + move[0]), (current_workshop[1] + move[1]))
            if ((0 <= new_workshop[0] < len(initial_state)) and (0 <= new_workshop[1] < len(initial_state[0])) and (initial_state[new_workshop[0]][new_workshop[1]] != 'x') and any(((district[0] <= new_workshop[0] <= district[1]) for district in districts)) and any(((district[0] <= current_workshop[0] <= district[1]) for district in districts))):
                new_cost = (g + 1)
                if ((new_workshop not in visited_costs) or (new_cost < visited_costs[new_workshop])):
                    visited_costs[new_workshop] = new_cost
                    h = heuristic(new_workshop, end_workshop)
                    heapq.heappush(queue, ((new_cost + h), new_cost, (actions + [new_workshop]), new_workshop))
    return None

def heuristic(current_workshop, end_workshop):
    return ((((current_workshop[0] - end_workshop[0]) ** 2) + ((current_workshop[1] - end_workshop[1]) ** 2)) ** 0.5)
print(a_star())
