foo = [i for i in input().split(" ") if i != ""]
tmp = {}
for i in foo:
    if i not in tmp:
        tmp[i] = 0
    if i in tmp:
        tmp[i] += 1
for i in tmp:
    if tmp[i] > 1:
        foo.remove(i)
print(*foo)
#print(tmp)
