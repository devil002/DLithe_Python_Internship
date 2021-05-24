#

t_case = int(input())
count = 0
num = []
print("Input : ")
while count < t_case:
    num.append([int(i) for i in input().split(" ") if i != ""])
    count += 1

print("Output : ")
for n in num:
    foo = int(n[2]/min(n[0],n[1]))
    print(str(foo))
