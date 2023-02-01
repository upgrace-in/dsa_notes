class Solution:
    def nextGreaterElement(self, nums1, nums2):
        if (len(nums1) == 0 and len(nums2) == 0):
            return nums1
        
        i = 0
        
        def check_for_rest(nums2, j, currEle):
            for k in range(j, len(nums2)-1):
                if nums2[k] > currEle:
                    return nums2[k]
            return -1
        
        while i < len(nums1):
            currEle = nums1[i]
            for j in range(0, len(nums2)):
                if currEle == nums2[j]:
                    nums1[i] = check_for_rest(nums2, j+1, currEle)
            i += 1
        
        return nums1
        

s = Solution()
print(s.nextGreaterElement([4,1,2], [1,3,4,2]))
        