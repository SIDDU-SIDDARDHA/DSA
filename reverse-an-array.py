class Solution:
    def reverseArray(self, arr):
        n = len(arr)

        for i in range(n // 2):
            temp = arr[i]
            arr[i] = arr[n - i - 1]
            arr[n - i - 1] = temp


if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]

    obj = Solution()          # create object
    obj.reverseArray(arr)    # call method correctly

    for i in range(len(arr)):
        print(arr[i], end=" ")
