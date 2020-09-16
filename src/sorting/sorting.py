# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    a = 0
    b = 0
    k = 0

    # Your code here
    # print("Arrays:", arrA, arrB)
    # for item in merged_arr:
    #     if arrA and arrB:
    #         print(arrA[0], arrB[0])
    #     if not arrA:
    #         item = arrB[0]
    #     elif not arrB:
    #         item = arrA[0]
    #     elif arrA[0] > arrB[0]:
    #         item = arrB[0]
    #         del arrB[0]
    #     elif arrB[0] > arrA[0]:
    #         item = arrA[0]
    #         del arrA[0]
    #     print("Merged:", merged_arr)

    # for i in range(len(merged_arr)):
    #     # print(a, b)
    #     # print(arrA[a], arrB[b])
    #     if a >= len(arrA):
    #         merged_arr[i] = arrB[b]
    #         b += 1
    #     elif b >= len(arrB):
    #         merged_arr[i] = arrA[a]
    #         a += 1
    #     elif arrA[a] < arrB[b]:
    #         merged_arr[i] = arrA[a]
    #         a += 1
    #     else:
    #         merged_arr[i] = arrB[b]
    #         b += 1
    # print(i, merged_arr[i])
    # if not arrA:
    #     print("Nothing in A.")
    #     merged_arr[i] = arrB[0]
    # elif not arrB:
    #     print("Nothing in B.")
    #     merged_arr[i] = arrA[0]
    # elif arrA[0] > arrB[0]:
    #     merged_arr[i] = arrB[0]
    #     del arrB[0]
    # elif arrB[0] > arrA[0]:
    #     merged_arr[i] = arrA[0]
    #     del arrA[0]

    # for i in range(len(merged_arr)-1):
    #     print(arrA, arrB)
    #     if not arrA:
    #         merged_arr[i] = arrB.pop(0)
    #     elif not arrB:
    #         merged_arr[i] = arrA.pop(0)
    #     elif arrA[0] < arrB[0]:
    #         merged_arr[i] = arrA.pop(0)
    #     else:
    #         merged_arr[i] = arrB.pop(0)
    #     print(merged_arr)

    """
    move through each element of merged_arr
    if the selected element in arrA is smaller than the element in arrB:
        add the selected element in arrA to merged_arr
        increment the pointer for arrA
    """
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr[k] = arrA[a]
            a += 1
        else:
            merged_arr[k] = arrB[b]
            b += 1
        k += 1
    while a < len(arrA):
        merged_arr[k] = arrA[a]
        a += 1
        k += 1
    while b < len(arrB):
        merged_arr[k] = arrB[b]
        b += 1
        k += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if (len(arr) == 1):
        print("SINGLE:", arr)
        return arr

    midIndex = len(arr) // 2
    print("Start:", 0, "End:", len(arr), "Last Element:", arr[len(arr)-1])
    print("Middle Index: ", midIndex)
    arr1 = arr[:midIndex]
    arr2 = arr[midIndex:]
    print(arr1, arr2)

    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)

    return merge(arr1, arr2)

# # STRETCH: implement the recursive logic for merge sort in a way that doesn't
# # utilize any extra memory
# # In other words, your implementation should not allocate any additional lists
# # or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here
