class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        
        n=len(arr)
        
        d = d % n
        
        #Reverse the first d elements
        
        self.reverse(arr, 0 , d - 1)
        
         #reverse the remaining n-d elements
         
        self.reverse(arr, d , n - 1)
         
         #reverse the entire array
         
        self.reverse(arr, 0 , n - 1)
         
         #function to reverse a portion of the array
         
    def reverse(self,arr,start,end):
        
             while start < end:
                 arr[start],arr[end]=arr[end],arr[start]
                 start += 1
                 end -= 1
                 
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5,]
    d = 2

    obj = Solution()          # create object
    obj.rotateArr(arr, d)    # call method correctly

    for i in range(len(arr)):
        print(arr[i], end=" ")  