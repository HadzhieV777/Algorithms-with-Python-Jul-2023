# 1. Binary Search

def binary_search(nums, target):
    first_index = 0
    last_index = len(nums) - 1

    while first_index <= last_index:
        middle_index = (last_index + first_index) // 2
        middle_element = nums[middle_index]

        if middle_element == target:
            return middle_index

        if target > middle_element:
            first_index = middle_index + 1
        else:
            last_index = middle_index - 1

    return - 1



nums = [int(x) for x in input().split()]
target = int(input())

print(binary_search(nums, target))
