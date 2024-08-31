# 2. You’re given a string where multiple
# characters are repeated consecutively. You’re supposed to reduce the size of
# this string using mathematical logic given as in the example below:
# •Input =
# abbbccddddde
# •Output = ab3c2d5e
# What is the time complexity of your
# code?


def compress_string(s):
    if not s:
        return ""

    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1])
            if count > 1:
                compressed.append(str(count))
            count = 1

    compressed.append(s[-1])
    if count > 1:
        compressed.append(str(count))

    return "".join(compressed)


input_str = "abbbccddddde"
output_str = compress_string(input_str)
print(output_str)  

# complexity : O(n)
