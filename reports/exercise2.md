# Bug reports for exercise2.py

Line: 13
Problem: The clamp function incorrectly returns `max(low, min(x, low))`, which always returns `low` when `x` is less than or equal to `low`, and incorrectly handles the upper bound logic.
Example: clamp(3, 1, 10) returns 1, which is correct, but clamp(15, 1, 10) returns 10, which is correct; however, the logic `min(x, low)` is wrong because it should be `min(x, high)`.
Fix: return max(low, min(x, high))
