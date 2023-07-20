def Magic(a):
    sum=0
    for i in str(a):
        
        sum += int(i)
    if sum>9:
        return Magic(sum)
    if sum == 1:
        return 1
    else :
        return 0


a =int(input())
print(Magic(a))


