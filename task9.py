a=[1,2,3,4,5,6,789,78,6,74,52,47,8]
f=0
n=0
for i in a:
    if(i%2==0):
        f+=1
    else:
        n+=1
print("No of even numbers in",a,"is",f)
print("No of odd numbers in", a,"is",n)