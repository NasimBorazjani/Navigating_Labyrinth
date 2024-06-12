
import heapq

def initialize():
    coins = [20, 25, 10, 4, 13, 3, 10, 17, 5, 25, 17, 2, 19, 24, 25, 10, 19, 8, 2, 20, 15, 84, 23, 87, 19, 8, 12, 17, 23, 6]
    tax_values = {12: 12, 19: 8, 84: 20, 24: 1, 5: 1, 3: 1, 4: 2, 87: 7, 10: 5, 25: 7, 6: 5, 20: 5, 15: 7, 23: 17, 13: 4, 17: 16, 2: 1, 8: 5}
    target_sum = 250
    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0
    queue = [(0, 0, [], (0, 0, 0))]
    return (coins, tax_values, target_sum, visited_costs, queue)

def a_star():
    (coins, tax_values, target_sum, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        (total_value, prev_coin, total_tax) = state
        if (total_value == target_sum):
            return actions
        for coin in coins:
            if ((coin not in actions) and ((total_value + coin) <= target_sum)):
                if (((coin < prev_coin) and ((coin % 2) == 0)) or ((coin >= prev_coin) and ((coin % 2) != 0))):
                    coin_tax = tax_values[coin]
                    new_total_tax = (total_tax + coin_tax)
                    new_state = ((total_value + coin), coin, new_total_tax)
                    new_cost = (g + coin_tax)
                    if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, ((g + new_total_tax), new_cost, (actions + [coin]), new_state))
    return None
print(a_star())
