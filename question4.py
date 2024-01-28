num = int(input("enter a number"))
a = 0
b = 1
sum = a + b
count = 1
while(count <= num):
    a = b
    b = sum 
    sum = a + b
    print(a)
    count += 1
