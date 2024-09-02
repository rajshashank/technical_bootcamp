def max_product(arr):
    if len(arr) < 2:
        return "Array should have at least two elements"

    arr.sort()

    product1 = arr[-1] * arr[-2]
    product2 = arr[0] * arr[1]

    return max(product1, product2)

array = [1, 20, -5, 4, -6, 7, 8]
result = max_product(array)
print("Maximum product of any two numbers in the array is:", result)
