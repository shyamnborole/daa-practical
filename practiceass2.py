def printjobscheduling(arr,t):
    n=len(arr)
    for i in range(n):
        for j in range (n-1-i):
            if arr[j+1][2]>arr[j][2]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    result=[False]*t
    job=["-1"]*t
    for i in range(n):
        for j in range(min(t-1,arr[i][1]-1),-1,-1):
            if result[j] is False:
                result[j]=True
                job[j]=arr[i][0]
                break
    print(job)
    
arr=[["q1",1,7],["q2",3,9],["q3",2,8],["q4",4,10]]
printjobscheduling(arr,3)