def printjobscheduling(arr, t):
    n=len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j+1][2]>arr[j][2]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    result=[False]*t
    job=[-1]*t
    for i in range(n):
        for j in range(min(t-1,arr[i][1]-1),-1,-1):
            if(result[j]==False):
                result[j]=True
                job[j]=arr[i][0]
                break
    print(job)
        


arr = [["J1",1,10],["J2",2,15],["J3",2,20],["J4",3,5],["J5",3,1]]
printjobscheduling(arr,3)
        
        