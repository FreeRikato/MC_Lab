def print_numbers(n, current=1):
    """
    Recursively print numbers from 1 to n.

    Parameters:
    n : int
        The upper limit of numbers to print.
    current : int
        The current number to print. This is used for the recursion and should not be
        set when calling this function initially.

    Description:
    This function starts by printing the current number, then it calls itself with the
    next number, until it reaches the number n. This demonstrates the concept of
    recursion where a function calls itself to achieve a repetitive task.
    """
    if current > n:
        return  # Base case: if current exceeds n, stop the recursion
    print(current)  # Print the current number
    print_numbers(n, current + 1)  # Recursive call with the next number

# Example usage:
# Print numbers from 1 to 10
print_numbers(10)
