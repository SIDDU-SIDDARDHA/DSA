class Solution:
    def nextPermutation(self, arr):
        n = len(arr)

        # Step 1: find the pivot
        pivot = -1
        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                pivot = i
                break

        # Step 2: If pivot does not exist, reverse entire array
        if pivot == -1:
            arr.reverse()
            return

        # Step 3: find element greater than pivot from right
        for i in range(n - 1, pivot, -1):
            if arr[i] > arr[pivot]:
                arr[i], arr[pivot] = arr[pivot], arr[i]
                break

        # Step 4: reverse the part after pivot
        left, right = pivot + 1, n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1


# Driver Code
if __name__ == "__main__":
    arr = [2, 4, 1, 7, 5, 0]

    obj = Solution()          # class name must be Solution
    obj.nextPermutation(arr)

    print("Next Permutation:")
    for x in arr:
        print(x, end=" ")
