def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


# when defining recursive functions you need a base case
#
# n = int(input("What do you want to factor :) ? "))
result = factorial(3)
