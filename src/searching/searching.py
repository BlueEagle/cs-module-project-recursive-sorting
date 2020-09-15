# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    midIndex = int((end-start)/2+start)
    if midIndex not in range(len(arr)):
        return -1
    mid = arr[midIndex]
    if target > mid:
        return binary_search(arr, target, midIndex+1, end)
    elif target < mid:
        return binary_search(arr, target, start, midIndex-1)
    elif target == mid:
        return midIndex
    else:
        return -1

    # # STRETCH: implement an order-agnostic binary search
    # # This version of binary search should correctly find
    # # the target regardless of whether the input array is
    # # sorted in ascending order or in descending order
    # # You can implement this function either recursively
    # # or iteratively
    # def agnostic_binary_search(arr, target):
    #     # Your code here
