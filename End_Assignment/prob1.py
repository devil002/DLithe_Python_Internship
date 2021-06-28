def isPrime(num):
    val = True
    if num > 1:
        for i in range(2, num):
            if (num%i) == 0:
                val = False
                break
        else:
            val = True
    return val

#print(isPrime(int(input())))
zee = int(input())
bar = [int(i) for i in range(2, zee) if isPrime(i)]
x = 0
tmp = []
for i in bar:
    x+=i
    if x <= zee:    tmp.append(i)
print(*tmp,sep=' + ')
