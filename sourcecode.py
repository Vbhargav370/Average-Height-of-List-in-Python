#Average of Heights in List
lis = list(map(int, input("Enter the Elements: ").split()))
sum = 0
for i in lis:
    sum += i
length = len(lis)    
print(sum/length)    
