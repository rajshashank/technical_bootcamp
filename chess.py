# check the validity of a knight move with current position and moved position as input

x = [3, 3]

print("valid moves")
for i in range(1, 8):
    for j in range(1, 8):
        if (abs(x[0] - i) + abs(x[1] - j) == 3):
            print("(", i, ",", j, ")")
