file = input("enter file with full name :")
list1 = []
with open(file,"r") as a:
    lines = a.readlines()
    for i in lines:
        list1.append(i.strip())
print(list1)
