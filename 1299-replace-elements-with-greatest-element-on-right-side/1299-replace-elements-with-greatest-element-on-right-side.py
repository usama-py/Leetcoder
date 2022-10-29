class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # if len(arr) == 1:
        #     return [-1]
        largest = arr[len(arr)-1]
        arr[len(arr)-1] = -1
        for i in range(len(arr)-2,-1,-1):
            temp = arr[i]
            arr[i] = largest
            if temp > largest:
                largest = temp
        return arr
        