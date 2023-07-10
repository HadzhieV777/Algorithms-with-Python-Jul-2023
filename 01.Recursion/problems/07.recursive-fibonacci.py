# 7. Recursive Fibonacci

def calc_fib(number):
    num1 = 1
    num2 = 1
    result = 0
    for num in range(number - 1):
        result = num1 + num2
        num1 = num2
        num2 = result
    return result


n = int(input())
print(calc_fib(n))
