# Bug reports for exercise2.py

Line: 3
Problem: is_passing returns True for grades strictly greater than 5, but the docstring states "True if the grade is 5 or more", which should include 5.
Example: is_passing(5) returns False, expected True.
Fix: return grade >= 5

Line: 8
Problem: is_valid_password does not check for at least one digit when the password is exactly 8 characters long; it only checks length > 8, which means it fails for valid passwords like "password1".
Example: is_valid_password("password1") returns False, expected True.
Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 12
Problem: clamp incorrectly uses min(x, low) and then max(low, min(x, low)), which results in always returning low, regardless of x.
Example: clamp(10, 1, 5) returns 1, expected 5.
Fix: return max(low, min(x, high))
