# 02. Selection Sort

nums = [int(x) for x in input().split()]

for index in range(len(nums)):
    current_number = nums[index]
    min_number = current_number
    min_index = index

    for next_index in range(index + 1, len(nums)):
        next_number = nums[next_index]

        if next_number <= min_number:
            min_number = next_number
            min_index = next_index

    nums[index], nums[min_index] = nums[min_index], nums[index]

print(*nums, sep=" ")
