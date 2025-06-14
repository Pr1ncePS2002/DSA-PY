def even_odd(num):
    if num%2==0 and num!=0:
        print(f"{num} is even")
    elif num==0:
        print(f"{num} is a whole number")
    elif num==1:
        print(f"{num} is neither even nor odd")
    else:
        print(f"{num} is odd")
        
x=int(input("enter number to check:"))
even_odd(x)