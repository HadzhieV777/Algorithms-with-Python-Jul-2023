# 3. Bubble Sort

def bubble_sort_with_nested_cycles(nums):
    for i in range(len(nums)):
        for j in range(1, len(nums) - i):
            if nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]

def bubble_sort(nums):
    is_sorted = False
    sorted_cells = 0

    while not is_sorted:
        is_sorted = True
        for index in range(1, len(nums) - sorted_cells):
            if nums[index] < nums[index - 1]:
                nums[index], nums[index - 1] = nums[index - 1], nums[index]
                is_sorted = False
        sorted_cells += 1


nums = [int(x) for x in input().split()]

bubble_sort(nums)

print(*nums, sep=' ')
