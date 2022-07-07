# Binary search

class Solution:

    def __init__(self, arr, query):
        self.arr = arr
        self.query = query
        self.dont_try = True

    def first_ele(self):  # 8
        # Predicate Formula
        # nums[x] >= target
        # FFFTTT
        lo, hi = 0, len(self.arr)-1
        while(lo < hi):
            mid = lo + (hi-lo) // 2
            if self.arr[mid] >= self.query:
                hi = mid
            else:
                lo = mid+1

        # Sanity Check
        if self.arr[lo] == self.query:
            return lo
        else:
            self.dont_try = False
            return None

    def last_ele(self):  # 10
        # Predicate Formula
        # nums[x] > target
        # TTTFFF
        if(self.dont_try != False):
            lo, hi = 0, len(self.arr)-1
            while(lo < hi):
                mid = lo + (hi-lo+1)//2
                if self.arr[mid] > self.query:
                    hi = mid-1
                else:
                    lo = mid

            return lo
        else:
            return None


arr = [0, 0, 0, 2, 2, 3, 4, 4, 6, 6, 6, 9, 9]
query = 5

s = Solution(arr, query)
print(s.first_ele(), s.last_ele())

# Plain english solution
# Get a predicate formula like
