nums=[5,10,15]
div=2
incompatible=[]
while div < 10:
    for num in nums:
        if num % div == 0:
            pass
        else:
            incompatible.append(div)
            print(incompatible)
            break
    
    div+=1
for x in range(2,10):
    if x in incompatible:
        gcd=1
        print(gcd)
        pass
    else:
        gcd(10,15,5)
        print("comdivisor:",x)
print("Gcd",gcd)
def gcd(*args):
    multilist=[]
    for num in args:
        multiples=2
        while multiples <= num:
            if num % multiples == 0:
                multilist.append(multiples)
            else:
                pass
            multiples+=1
    common=[]
    for each in multilist:
        frequency=multilist.count(each)
        if frequency > 1:
            common.append(each)
        else:
            pass
    gcd=max(common)
    print("Gcd=",gcd)
            
            
        

