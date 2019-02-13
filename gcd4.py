def numbers():
    numbers=[]
    while True:
        try:
            no_of_nums=int(input("Enter number of entries:"))
            break
        except ValueError:
            print("Number of entries must be in digits mamen!!")
    count=1
    while len(numbers) < no_of_nums:
        try:
            nums=int(input("Enter number %d:" % (count)))
            numbers.append(nums)
            
        except ValueError:
            print("Only digits mamen!!")
        count+=1
    return numbers

numbers=numbers()    
def gcd(*args):
    multilist=[]
    for num in args:
        count=1
        while count <= num:
            if num % count == 0:
                multilist.append(count)
            else:
                pass
            count+=1
    
    length=len(args)
    common=[]
    for no in multilist:
        frequency=multilist.count(no)
        if frequency == length:
            common.append(no)
        else:
            pass
    
    gcd=max(common)
    print("GCD:",gcd)

gcd(*numbers)
