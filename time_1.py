# 750005 seconds in how many days,hours,minutues and seconds
x = 750005

d = 86400
h = 3600
m = 60

days = x // d
hour = (x - days * d) // h
min = (x - (days * d + hour * h)) // m
sec = x % 60


print(days , "Days" , hour , "Hours" , min , "Mins" , sec , "Sec")