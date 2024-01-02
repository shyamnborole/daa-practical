def largenum(x,y):
    if(x<10):
        return x*y
    else:
        n=len(str(x))
        h=n//2
        p=10**h
        k=100*h
        a=x//p
        b=x%p
        ac=largenum(a,a)
        bd=largenum(b,b)
        plus=largenum(a+b,a+b)-(ac+bd)
        return ac* k + plus * p + bd
x=input("enter ur num")
print(largenum(int(x),int(x)))


    
