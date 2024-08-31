# Problem Statement – An automobile company manufactures both a two wheeler(TW) and a
# four wheeler(FW). A company manager wants to make the production of both types of
# vehicle according to the given data below:

# 1st data, Total number of vehicle(two-wheeler + four-wheeler) = v
# 2nd data, Total number of wheels = W
# The task is to find how many two-wheelers as well as four-wheelers need to manufacture as
# per the given data.
# Example:

# Input:
# 200 - &gt
# Value of V
# 540 - &gt
# Value of W

# Output:
# TW = 130 FW = 70

# Explanation:
# 130+70 = 200 vehicles
# (70*4)+(130*2) = 540 wheels


def find_vehicles(V, W):
    if W % 2 != 0 or W < 2 * V or W > 4 * V:
        return "No solution possible"

    TW = (4 * V - W) // 2
    FW = V - TW
    return TW, FW


# Example usage
V = 200
W = 540
result = find_vehicles(V, W)
print(f"TW = {result[0]} FW = {result[1]}")
