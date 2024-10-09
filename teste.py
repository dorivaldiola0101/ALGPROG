x = 1 

while x !=0:
    x = int(input())
    if x !=0:
        for i in range(1,x+1):
            if i == x:
                print(i, end="")
            else:
                print(i, end=" ")
        print()
            
