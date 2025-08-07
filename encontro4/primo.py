n = int(input())

x = True
if n < 2:
    print('N')
elif n == 2:
    print("Y")
elif n % 2 == 0 :
    print('N')    
else:
    for i in range(3,int((n**0.5))+1,2):
        a = n%i
        #print (a)
        if a== 0:
           x = False
           break

    if x == True:
        print('Y')
    else:
        print('N')