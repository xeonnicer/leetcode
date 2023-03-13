# bubble sort
from typing import List


def bubble_sort(nums: List[int]):
    length = len(nums)
    for i in range(length - 1):
        for j in range(0, length - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return


def pick_sort(nums: List[int]):
    length = len(nums)
    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if nums[j] < nums[min_index]:
                min_index = j

        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]
    return


def quick_sort(nums: List[int], left, right):
    def partition(arr, left, right):
        pivot = arr[left]
        while left < right:
            while left < right and arr[right] >= pivot:
                right -= 1
            arr[left] = arr[right]
            while left < right and arr[left] <= pivot:
                left += 1
            arr[right] = arr[left]
        arr[left] = pivot
        return left

    if left < right:
        mid = partition(nums, left, right)
        quick_sort(nums, left, mid - 1)
        quick_sort(nums, mid + 1, right)


nums = [9, 2, 67, 77, 2, 5, 200, 0, 9]
nums = [8, 1, 9, 17, 19, 97]
nums = [5, 7, 4, 6, 3, 1, 2, 9, 8]

# bubble_sort(nums)
# pick_sort(nums)
# quick_sort(nums, 0, len(nums) - 1)
# print(nums)



