def func_count(list):
    list1 = set(list)
    for i in list1:
        count = list.count(i)
        print(f"{i}:{count}occurences")

func_count((1,2,3,4,4,4,5,5,7,7,7,8,8,8,8,8,8,9,9,0,5,5))        
