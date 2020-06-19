# ch2_6.py
from array import *
x = array('i', [5, 15, 25, 35, 45])     # 建立無號整數陣列

# pop(i) 可以回傳&刪除index i 的元素，若省略i相當於i=-1，回傳&刪除最後一個元素
n = x.pop()
print('刪除 ', n)
for data in x:
    print(data)

n = x.pop(2)
print('刪除 ', n)
for data in x:
    print(data)









