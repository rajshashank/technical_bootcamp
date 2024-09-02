# merge two arrays and sort it
# a = [2,8,15,18,20,25,32]
# b = [3,5,11,16,19]
# out = []

# i = 0
# j = 0

# while i <= len(a) | j <= len(b):
#     if a[i] < b[i]:
#         out.append(a[i])
#         i += 1
#     elif a[i] > b[i]:
#         out.append(b[i])
#         j += 1

# print(out)

a = [2, 8, 15, 18, 20, 25, 32]
b = [3, 5, 11, 16, 19]
out = []

i = 0
j = 0

while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        out.append(a[i])
        i += 1
    else:
        out.append(b[j])
        j += 1

while i < len(a):
    out.append(a[i])
    i += 1

while j < len(b):
    out.append(b[j])
    j += 1

print(out)






# c = a + b
# n = len(c)
# for i in range(n):
#     for j in range(0, n - i - 1):
#         if c[j] > c[j + 1]:
#             c[j], c[j + 1] = c[j + 1], c[j]

# print(c)


