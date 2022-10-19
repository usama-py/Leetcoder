class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        maxi = -1
        index = 0
        if len(arr) <= 2:
            return False
        for i in range(len(arr)):
            if i >= len(arr)-1:
                return False
            if arr[i] == arr[i+1]:
                return False
            if arr[i+1] < arr[i] and i <= len(arr)-1:
                maxi = arr[i]
                index = i
                break
        if index == 0 or index == len(arr)-1:
            return False
        for i in range(index+1,len(arr)):
            if arr[i] == maxi or arr[i] > maxi:
                return False
            if i < len(arr)-1:
                if arr[i] <= arr[i+1]:
                    return False
        return True
            
            