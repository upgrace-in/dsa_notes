# Find minimum in rotated list

# Brute Force Solution
def nums_of_rotation(nums):
    for i in range(len(nums)-1):
        if nums[i+1] < nums[i]:
            return (len(nums) - i)-1


#Optimal Solution
def optimal_rotation_func(nums):
    lo, hi = 0, len(nums)-1
    while(lo < hi):
        mid = lo + (hi-lo)//2
        if nums[mid] < nums[0]:
            hi = mid
        else:
            lo = mid+1

    if(nums[lo] < nums[0]):
        return nums[lo]
    else:
        return nums[0]

nums = [11, 13, 15, 17]
print(optimal_rotation_func(nums))
