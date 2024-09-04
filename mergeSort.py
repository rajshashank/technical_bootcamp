def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    # Merge the two halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append the remaining elements (if any)
    result.extend(left[i:])
    result.extend(right[j:])

    return result

arr = [8, 3, 1, 7, 0, 10, 2]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
