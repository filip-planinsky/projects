
def fibonacci(n):
    """
    calculating fibonacci of n
    """
    # defining initial values for first two Fibonacci Numbers and count
    fib1, fib2, count, fibN = 0, 1, 0, 0

    # declaring dict for storing Key and values for Fibonacci numbers
    # initialising first and second fibNumber
    fib_numbers = {0: fib1, 1: fib2}

    # if given number is 0 or 1 we can directly return FibNumber from dict
    if n in fib_numbers:
        print(f"Fibonacci {n} is: {fib_numbers[n]}")

    else:
        # calculating fiboNumber as long as we reach the given number
        while count <= n:
            # adding Key and Value to fib_numbers dict
            fib_numbers[count] = fib1
            fibN = fib1 + fib2

            # updating values
            fib1 = fib2
            fib2 = fibN

            # updating count
            count += 1
        print(f"Fibonacci {n} is: {fib_numbers[n]}")


if __name__ == "__main__":

    fibOf = int(input("What is Fibonacci of:  "))
    fibonacci(fibOf)
