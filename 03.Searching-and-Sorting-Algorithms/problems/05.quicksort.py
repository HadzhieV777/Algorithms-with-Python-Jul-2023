# 5. Quicksort

def quicksort(start_index, end_index, nums):

    if start_index >= end_index:
        return

    pivot = start_index
    left = start_index + 1
    right = end_index

    while left <= right:
        if nums[left] > nums[pivot] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]

        if nums[left] <= nums[pivot]:
            left += 1

        if nums[right] >= nums[pivot]:
            right -= 1

    nums[pivot], nums[right] = nums[right], nums[pivot]
    quicksort(start_index, right - 1, nums)
    quicksort(left, end_index, nums)


nums = [int(x) for x in input().split()]

quicksort(0, len(nums) - 1, nums)

print(*nums, sep=' ')
