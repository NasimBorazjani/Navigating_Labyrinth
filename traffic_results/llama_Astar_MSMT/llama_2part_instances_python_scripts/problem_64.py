
import heapq

def initialize():
    initial_state = (('8', '12', '16', 'x', 'x', '7', 'x', 'x', 'x', 'x', 'x'), ('x', 'x', 'x', 'x', '16', '7', '8', '17', '19', 'x', 'x'), ('7', 'x', '13', '19', '6', '14', '18', 'x', '19', 'x', 'x'), ('9', '20', '2', '10', '6', 'x', '18', 'x', 'x', 'x', '18', 'x'), ('x', 'x', '8', '12', '7', '14', '13', '9', '8', '6', '14', '11', '7'), ('x', '14', 'x', 'x', 'x', '19', '13', '15', '3', '12', '16', '16', '3'), ('x', 'x', 'x', '13', '9', '13', '10', 'x', '14', 'x', '4', '18'), ('6', '12', '10', 'x', 'x', '18', '7', '20', '18', 'x', '13', '1', 'x'), ('x', '5', 'x', '18', '12', 'x', 'x', '3', '12', '16', '16', 'x', '8'), ('10', 'x', '19', 'x', 'x', 'x', '11', '14', '16', '12', 'x', '8'), ('8', 'x', 'x', 'x', 'x', 'x', '9', '16', '15', 'x', 'x', '8'), ('x', 'x', '2', 'x', '1', 'x', 'x', '3', 'x', 'x', 'x'), ('9', 'x', '5', 'x', 'x', '15', 'x', 'x', '7', '15', '9', 'x', 'x'))
    start_workshop = (0, 0)
    end_workshop = (11, 11)
    districts = [(0, 3), (4, 5), (6, 11)]
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
