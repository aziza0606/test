n=int(input("n ni kiriting:"))

count=0
sum=0

for i in range(1,n+1):
    if i%2==0:
        count+=1
      
for i in range(1,n+1):
    if i%2!=0:
        sum+=1
       
print("toqlar son:",sum)
print("juftlar soni:",count)
