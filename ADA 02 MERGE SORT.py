def merge(left, right):

    merged_list = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:

            merged_list.append(right[j])
            j += 1

        else:
            merged_list.append(left[i])
            i += 1
    merged_list += left[i:]
    merged_list += right[j:]

    return merged_list


def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


x = merge_sort([1,5,7,89,23,5768,8,43])
print(x)