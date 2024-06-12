
import heapq

def initialize():
    coins = [19, 11, 35, 3, 12, 23, 42, 45, 8, 12, 32, 82, 39, 12, 45, 12, 40, 38, 28, 6, 32, 37, 39, 9, 43, 12, 38, 4, 42, 44, 41, 37, 83, 5, 38]
    tax_values = {37: 6, 43: 18, 32: 16, 4: 4, 83: 4, 8: 5, 23: 18, 12: 6, 82: 16, 44: 20, 39: 1, 19: 8, 35: 7, 38: 11, 11: 3, 42: 5, 45: 12, 3: 1, 6: 2, 41: 3, 28: 18, 40: 2, 9: 6, 5: 4}
    target_sum = 466
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
