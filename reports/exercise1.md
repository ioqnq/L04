# Bug reports for exercise1.py

Line: 3
Problem: The function is_even returns True for odd numbers because it checks if n % 2 == 1, which is incorrect for even numbers.
Example: is_even(2) returns False, but it should return True; is_even(3) returns True, which is incorrect.
Fix: return n % 2 == 0

Line: 8
Problem: The rectangle_area function returns the sum of width and height, but it should return the product (area) of width and height.
Example: rectangle_area(4, 5) returns 9, but expected 20.
Fix: return width * height

Line: 12
Problem: The double function adds 2 to n, but the docstring says "twice the number n", which means it should multiply by 2.
Example: double(3) returns 5, but expected 6.
Fix: return n * 2
