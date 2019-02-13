def gcd(*args,length):
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
    print(multilist)
    print(common)
    gcd=max(common)
    if common.count(gcd) != length:
        common.remove(gcd)
        gcd=max(common)
    print("Gcd=",gcd)
nums=[70,49,35]
length=len(nums)
print("length of nums: ",len(nums))
gcd(*nums,length)
