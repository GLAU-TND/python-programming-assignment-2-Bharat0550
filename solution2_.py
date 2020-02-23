lst1=[10,7,76,415]
khali_list=[]
for i in lst1:
    if i<=9:
        khali_list.insert(0,i)
    elif i>=11 and i<=100:
        khali_list.insert(1,i)
    elif i>=100 and i<=999:
        khali_list.insert(2,i)
    elif i>=10 and i<=11:
        khali_list.insert(3,i)
for i in khali_list:
    print(i,end="")
