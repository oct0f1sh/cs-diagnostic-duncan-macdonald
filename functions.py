# Solution for problem 8


def fibonacci_iterative(num = 10):
    previous = 1
    precedingPrevious = 0
    for number in range(0,num):
        fibonacci = (previous + precedingPrevious)
        print(fibonacci)
        precedingPrevious = previous
        previous = fibonacci


# Solution for problem 9
# I don't know how to call stuff from the terminal and my python
# installation is really screwed up so I'm using PyCharm to run these
# and i'm just going to set an input


arg = int(input("Enter a number: "))

fibonacci_iterative(arg)

print()


# Solution for problem 10


def factorial_recursive(num):
    solution = num
    while num != 0:
        solution = solution * (num - 1)
        print(solution)
        num = num - 1

factorial_recursive(6)