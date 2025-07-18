# Coin Change Algorithm

This project implements a **dynamic programming** solution to the classic **coin change** problem.

Given a list of coin denominations and a target amount, it calculates:
- The minimum number of coins needed.
- Which coins are used to achieve that amount.

## How It Works

- The algorithm filters out coin denominations larger than the target amount.
- It uses a dynamic programming (DP) array to compute the minimum coins required for each amount up to the target.
- It reconstructs the combination of coins used based on a tracking array.
- If no combination is possible, it returns `"no solution was found :("`.

> Note: This ensures the minimum number of coins is used.

## Example

```python
coins = [2, 5, 10, 20, 50, 100]
change = 53
result = get_coin_change(coins, change)
print("result: ", result)
```