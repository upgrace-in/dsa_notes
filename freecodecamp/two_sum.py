class Solution:
    def twoSum(self, nums, target):
        def check_for_the_match(ele, index, arr):
            for i in range(index, len(arr)):
                if(ele+nums[i] == target):
                    global final
                    final = [index-1, i]
                    print(final)
                    return True
            return False
                
        for i in range(0, len(nums)):
            if(check_for_the_match(nums[i], i+1, nums) != False):
                return final

s = Solution()
s.twoSum([0,4,3,0], 0)