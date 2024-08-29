# prog to compute auto fare with min 35 for 1.5 and 25 for every km


x = float(input("enter the distance : "))
# amt = 35
min_dist = 1.5

if x <= min_dist:
    amt = 35

else:
    amt = 35 + (int(x)-1) * 25

print(int(x))
print("Charges for ", x, " kms is Rs", amt)
