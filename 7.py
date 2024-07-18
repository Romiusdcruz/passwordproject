import random as rd

upper = ["A" , "B" , "C" , "D" , "E"]
lower = ['a', 'b', 'c', 'd', 'e']
num   = ['0', '1', '2', '3', '4']
all_char = upper + lower + num
pwd = rd.choice(upper) + rd.choice(lower)  + rd.choice(num) 
for i in range (0, 3, 1):
    a = rd.choice(all_char)
    pwd = pwd + a

print(pwd)
