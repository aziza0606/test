

for i in range (100,1000):
    birlik=i%10
    onlik=(i//10)%10
    yuzlik=i//100
    if birlik==onlik or onlik==yuzlik or yuzlik==birlik:
        print(i)