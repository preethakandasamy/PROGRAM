str=input()
m=[]
for i in str:
    if i not in m:
        m.append(i)
print(len(m))
