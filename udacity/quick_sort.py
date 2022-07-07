'''
Take a pivot (hold a ptr)
-compare with the 1st ele

if ele > pivot:
    put it on ptr
    move the ptr-1 ele to first pos
    place the pivot to ptr-1
else:
    left = left + 1
'''


def sort_it(nums, left, ptr):
    pivot = nums[ptr]
    while left < ptr:
        if nums[left] > pivot:
            nums[ptr] = nums[left]
            nums[left] = nums[ptr-1]
            ptr = ptr - 1
            nums[ptr] = pivot
        else:
            left = left + 1
    return ptr

def quick_sort(nums, start=0, end=None):
    if end is None:
        nums = list(nums)
        end = len(nums)-1

    if start < end:
        pivot = sort_it(nums, start, end)
        quick_sort(nums, start, pivot-1)
        quick_sort(nums, pivot+1, end)

    return nums

nums = [8, 3, 1, 0, 10, 2]
print(quick_sort(nums, 0, None))
