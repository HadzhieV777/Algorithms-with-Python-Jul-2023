# 02. Nested Loops to Recursion

def recursive_loop(index, array):
    if index >= len(array):
        print(*array, sep=' ')
        return

    for num in range(n):
        array[index] = num + 1
        recursive_loop(index + 1, array)


n = int(input())

array = [None] * n

recursive_loop(0, array)
