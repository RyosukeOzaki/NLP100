# coding: utf-8
p = 'パトカー'
t = 'タクシー'
list = []
for i,j in zip(p,t):
    list.append(i)
    list.append(j)
print("".join(list))
