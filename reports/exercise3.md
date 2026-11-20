# Bug reports for exercise3.py

Line: 3
Problem: The average function crashes when given an empty list because len(numbers) is 0, leading to division by zero.
Example: average([]) raises ZeroDivisionError.
Fix: return sum(numbers) / len(numbers) if numbers else 0

Line: 8
Problem: The first_word function returns an empty string for empty input, which is correct per docstring, but it fails if the text contains only whitespace (e.g., "  ").
Example: first_word("  ") returns '', which is correct, but first_word("  hello") returns 'hello', which is incorrect because it should return the first non-empty word.
Fix: return text.strip().split()[0] if text.strip() else ""

Line: 12
Problem: The percent function returns a division by zero when total is 0, even though the docstring says "If total is 0, the result is 0".
Example: percent(5, 0) raises ZeroDivisionError.
Fix: return part / total * 100 if total != 0 else 0
