x = int(input("Enter the number : "))
n = 0
sum = 0
while x != 0:
    n = x % 10 
    sum += n
    x //= 10
    
print("Sum of the digits : ",sum)