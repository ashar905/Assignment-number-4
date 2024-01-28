def gen_dict(n):
    dict1 = {}
    for i in range(1,n+1):
       dict1[i] = i*i
       if i == n:
           return dict1
print(gen_dict(6))
