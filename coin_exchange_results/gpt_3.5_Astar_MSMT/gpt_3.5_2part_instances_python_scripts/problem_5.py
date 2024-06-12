
import heapq

def initialize():
    coins = [20, 10, 16, 21, 15, 21, 13, 6, 19, 9, 7, 5, 2, 6, 9, 22, 4, 13, 3, 16, 22, 18, 6, 5, 14, 7, 7, 2, 17, 9, 8, 83, 14]
    tax_values = {22: 18, 21: 1, 14: 12, 10: 8, 8: 6, 17: 9, 6: 4, 7: 6, 9: 3, 20: 13, 19: 12, 5: 3, 13: 8, 4: 3, 83: 14, 3: 2, 18: 1, 2: 1, 16: 2, 15: 3}
    target_sum = 239
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
