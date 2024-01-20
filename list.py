from typing import List

list=['0','0','1','1','1','2','2','3','3','4']
list_1=set(list)
sort=sorted(list_1)
len1=len(sort)
len_1=len(list)
len_2=len_1-len1
for i in range(len_2):
    sort.append('_')
join=(','.join(sort))
print('[',join,']')
