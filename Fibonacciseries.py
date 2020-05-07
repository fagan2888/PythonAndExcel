# 0, 1, 1, 2, 3, 5, 8
def fibonacci(number):
    if number in [0, 1]:
        return number
    prev = number - 1
    beforePrev = number - 2
    sum = 0
    while beforePrev >= 0:
        sum = sum + fibonacci(prev) + fibonacci(beforePrev)
        prev = beforePrev
        beforePrev = prev - 1
        return sum


findFibonacciFor = input("Enter position to find fibonacci number for or 0 to exit:")
while int(findFibonacciFor) > 0:
    if int(findFibonacciFor) > 0:
        for num in range(int(findFibonacciFor)):
            print(fibonacci(num))
    findFibonacciFor = input(
        "Enter position to find fibonacci number for or 0 to exit:"
    )
