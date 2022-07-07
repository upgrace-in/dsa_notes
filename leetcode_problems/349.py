class Solution:
    def intersection(self, nums1, nums2):
        if (nums1 is None) or (nums2 is None):
            return []

        if (len(nums1) == len(nums2)) and (len(nums2) == 1):
            return nums1

        lst = []

        def find_key(key, nums):
            lo, hi = 0, len(nums)-1

            while lo < hi:
                mid = lo + (hi-lo)//2
                if nums[mid] < key:
                    lo = mid+1
                else:
                    hi = mid

            if nums[lo] == key:
                lst.append(key)
                
            return None

        if len(nums1) > len(nums2):
            nums1.sort()
            final_list = nums1
            iterating_list = nums2
        else:
            nums2.sort()
            final_list = nums2
            iterating_list = nums1

        for i in iterating_list:
            find_key(i, final_list)

        return list(set(lst))


s = Solution().intersection([1,2], [1,2])
print(s)