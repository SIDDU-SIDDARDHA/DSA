class Solution:
    def pushZerosToEnd(self, arr):
        count = 0

        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i], arr[count] = arr[count], arr[i]
                count += 1


if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]

    ob = Solution()                 # Create object
    ob.pushZerosToEnd(arr)          # Call using object

    for num in arr:
        print(num, end=" ")
