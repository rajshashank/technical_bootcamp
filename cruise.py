# 4) A party has been organised on cruise. 
# The party is organised for a limited time(T). 
# The number of guests entering (E[i]) and leaving (L[i]) 
# The task is to find the maximum number of guests present on the cruise
# at any given instance within T hours.

# Example 1:
# Input :

# 5 Value of T
# [7,0,5,1,3] E[], Element of E[0] to E[N-1]
# [1,2,1,3,4] L[], Element of L[0] to L[N-1] 
# Output : 8 Maximum number of guests on cruise at an instance.

def max_guests(t, e, l):
    current_guests = 0
    max_guests = 0

    for i in range(t):
        current_guests += e[i] - l[i]
        if current_guests > max_guests:
            max_guests = current_guests

    return max_guests

t = 1
e = [7, 0, 5, 1, 3]
l = [1, 2, 1, 3, 4]
if t <= len(e) :
    result = max_guests(t, e, l)
else:
    result = "Out of hours"
print(result)  
