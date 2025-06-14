# result=lambda a,b:a+b 
# print(result(5,6))

# result2=lambda a,b,c:a*b*c
# print(result2(6,7,9))

# even=lambda num:num%2==0
# print(even(24))

# numbers=[1,2,3,4,5,6]
# x=list(map(lambda x:x**2,numbers))
# print(x)

##filter takes first parameter a function and second a list
def even(num):
    if num%2==0:
        return True

lst=[1,2,3,4,5,6,7,8,9]
print(list(filter(even,lst)))

num=[3,4,5,6,7,8,9,33,4,5,3,2]
greater_5=list(filter(lambda x:x>5,num))
print(greater_5)