numbers=[]
while len(numbers) < 3:
    try:
        nums=int(input("Enter number(press enter to continue): "))
        numbers.append(nums)
        
    except ValueError:
        print("Only digits mamen!!")
    
print(numbers)

def compatibility(numbers):
    check=2
    complist=[]
    while check < 10:
        freq=0
        for num in numbers:
            if num % check == 0:
                freq+=1
            else:
                pass
        if freq == 3:
            complist.append("compatible")
        else:
            complist.append("incompatible")
        check+=1
    return complist
checked=compatibility(numbers)
def gcd(numbers):
    if "compatible" in checked:
        multilist=[]
        for num in numbers:
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
        print("GCD:",gcd)
    else:
        print("gcd=1")
gcd(numbers)


