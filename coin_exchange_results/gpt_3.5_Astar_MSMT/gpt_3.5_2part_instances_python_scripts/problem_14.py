
import heapq

def initialize():
    coins = [9, 18, 7, 20, 4, 12, 5, 5, 18, 5, 2, 11, 5, 16, 19, 8, 10, 9, 12, 14, 17, 6, 14, 16, 20, 10, 10, 13, 4, 13, 7, 14, 14, 10, 2, 7, 14, 11, 16, 10, 10, 5, 14, 20, 4, 17]
    tax_values = {17: 16, 8: 8, 6: 6, 16: 12, 5: 4, 14: 12, 18: 9, 12: 1, 19: 12, 4: 2, 7: 3, 10: 7, 11: 7, 13: 6, 2: 1, 9: 1, 20: 10}
    target_sum = 206
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
