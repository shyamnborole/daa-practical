def largemultiply(x,y):
    if(x<10):
        return x*y
    else:
        n=len(str(x))
        h=n//2
        p=10**h
        k=100**h
        a=x//p
        b=x%p
        ac=largemultiply(a,a)
        bd=largemultiply(b,b)
        plus=largemultiply(a+b,a+b)-(ac+bd)
        return ac * k + plus *p + bd
    
x=input("enter the number: ")
y=largemultiply(int(x),int(x))
print(y)
