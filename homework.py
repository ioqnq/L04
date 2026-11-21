def is_passing(grade):
    """True if the grade is 5 or more"""
    return grade > 5  # BUG: Should be >= 5


def is_valid_password(password):
    """At least 8 characters and at least one digit"""
    return len(password) > 8 and any(c.isdigit() for c in password)  # BUG: Should be len(password) >= 8


def clamp(x, low, high):
    """x, limited to the range from low to high"""
    return max(low, min(x, low))  # BUG: Should be min(x, high)


def filter_and_sum_evens(matrix):
    """Sum all even numbers present in a 2D grid (list of lists of integers)."""
    total = 0
    for row in matrix:
        for val in row:
            if val % 2 == 1:  # BUG: Checks for odd numbers instead of even (val % 2 == 0)
                total += val
    return total


def remove_duplicates_and_sort(numbers):
    """Removes duplicates from a list of numbers and returns them sorted in ascending order."""
    unique_numbers = list(set(numbers))
    unique_numbers.reverse()  # BUG: Reverses the list instead of sorting it (.sort())
    return unique_numbers