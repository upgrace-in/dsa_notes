def bubble_sort(nums):
    nums = list(nums)

    for _ in range(len(nums)-1):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

    return nums


def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i-1
        while j >= 0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1, cur)
        print(nums)
    return nums


def merge(nums1, nums2, depth=0):
    i, j, merged = 0, 0, []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    return merged + nums1[i:] + nums2[j:]


def merge_sort(nums, depth=0):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    return merge(merge_sort(nums[:mid], depth+1),
                 merge_sort(nums[mid:], depth+1),
                 depth+1)

def partition(nums, start=0, end=None):
    if end is None:
        end = len(nums)-1

    l, r = start, end-1

    while r > l:
        if nums[l] <= nums[end]:
            l += 1
        elif nums[r] > nums[end]:
            r -= 1
        else:
            nums[l], nums[r] = nums[r], nums[l]

    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end


def quick_sort(nums, start=0, end=None):
    if end is None:
        nums = list(nums)
        end = len(nums)-1

    if start < end:
        pivot = partition(nums, start, end)
        quick_sort(nums, start, pivot-1)
        quick_sort(nums, pivot+1, end)

    return nums


# Quick Sort then Try some problems and then continue DSA


nums = [2, 5, 3, 1, 10, 19, 4, 5]
print(quick_sort(nums))
