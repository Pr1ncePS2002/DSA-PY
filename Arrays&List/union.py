
x=[1,2,3,45,5,6,6]
y=[2,3,4,5,6]
z=[]
for i in x:
    if i in y:
        z.append(i)
print(list(set(z)))

        