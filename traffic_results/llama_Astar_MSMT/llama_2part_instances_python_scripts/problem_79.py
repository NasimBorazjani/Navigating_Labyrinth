
import heapq

def initialize():
    initial_state = (('x', '16', '15', '14', '2', '12', '3', 'x', '7', '7'), ('11', 'x', 'x', 'x', '4', '10', '5', 'x', 'x', 'x'), ('12', 'x', '3', 'x', 'x', 'x', 'x', 'x', 'x', 'x'), ('16', '15', '13', 'x', '12', 'x', 'x', '1', 'x', '7'), ('2', '6', 'x', '5', 'x', '14', '7', 'x', '8', '18'), ('19', '17', '2', '11', '8', '17', '12', '8', '9', '14'), ('11', '1', '10', '11', 'x', 'x', '19', '6', '2', '18'), ('7', 'x', '10', '15', 'x', 'x', 'x', 'x', '18', '17'), ('x', '6', 'x', 'x', 'x', '5', 'x', '7', '12', '20'), ('x', 'x', '2', '15', 'x', '17', 'x', 'x', '10', '11'))
    start_workshop = (4, 12)
    end_workshop = (7, 0)
    districts = [(0, 4), (5, 6), (7, 13)]
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
