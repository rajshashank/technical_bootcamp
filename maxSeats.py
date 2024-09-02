def max_consecutive_free_seats(arr):
    max_count = 0
    current_count = 0

    for seat in arr:
        if seat == 'S':
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count

seats = ['S', 'S', 'X', 'S', 'S', 'S', 'X', 'S', 'S']
result = max_consecutive_free_seats(seats)
print("Maximum seats that can be booked in a sequence:", result)
