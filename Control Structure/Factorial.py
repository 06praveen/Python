def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        print("The factorial of", n, "is 1.")
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        print("The factorial of", n, "is", result)

num = int(input("Enter a number to compute its factorial: "))
factorial(num)
