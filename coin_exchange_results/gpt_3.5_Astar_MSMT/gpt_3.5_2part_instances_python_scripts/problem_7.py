
import heapq

def initialize():
    coins = [41, 4, 22, 8, 5, 5, 20, 4, 3, 19, 4, 13, 3, 18, 20, 9, 15, 3, 3, 14, 3, 14, 9, 4, 15, 19, 6, 15, 22, 19, 3, 3, 20, 9, 20, 11, 22, 15, 20]
    tax_values = {20: 11, 15: 13, 9: 7, 8: 3, 3: 1, 6: 3, 5: 2, 13: 11, 4: 4, 22: 11, 19: 19, 11: 1, 14: 2, 41: 16, 18: 18}
    target_sum = 220
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
