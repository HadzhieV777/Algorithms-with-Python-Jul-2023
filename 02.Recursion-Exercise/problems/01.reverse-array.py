# 01. Reverse Array

def reverse_array(index, elements):
    if index == len(elements) // 2:
        return

    swap_index = len(elements) - 1 - index
    elements[index], elements[swap_index] = elements[swap_index], elements[index]
    reverse_array(index + 1, elements)


elements = input().split()

reverse_array(0, elements)

print(' '.join(elements))
