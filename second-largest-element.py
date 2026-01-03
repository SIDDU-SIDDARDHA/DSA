class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)
        if n < 2:
            return -1
            
        first = second = float('-inf')

        for num in arr:
            if num > first:
                second = first
                first = num
            elif num > second and num != first:
                second = num

        if second == float('-inf'):
            return -1
        else:
            return second


getSecondLargest = Solution().getSecondLargest
# Example :
print(getSecondLargest([2, 3, 6, 6, 5]))  # Output: 5
#example :