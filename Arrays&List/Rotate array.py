def rotate(x,k):
    
    k=k%len(x)
    y= x[-k:]+ x[:-k] 

    return y
z=[1,2,3,4,5,6,7]
z=rotate(z,2)
print(z)