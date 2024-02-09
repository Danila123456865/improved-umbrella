from typing import List
list=[0,1,0,0,1,0]
list_2=[0,1,0,1,1,0]

k=0
len_1=len(list_2)

while k!=len_1:
    k+=1
    if list[0]==list_2[0]:
        del list_2[0]
        del list[0]
    else:
        list.append(list[0])
        del list[0]
if k==len_1:
    len_12=len(list_2)
    print(len_12)



