class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)
        if n < 2:
            return -1
        
        max1 = float('-inf')
        max2 = float('-inf')
        
        for i in range(n):
            if arr[i] > max1:
                max2 = max1
                max1 = arr[i]
            elif arr[i] > max2 and arr[i] != max1:
                max2 = arr[i]
        
        if max2 == float('-inf'):
            return -1
        else:
            return max2

arr = [100, 200, 760, 900, 786]
sol = Solution()
result = sol.getSecondLargest(arr)
print(result)
