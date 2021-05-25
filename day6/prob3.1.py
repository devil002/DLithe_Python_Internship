# A little girl living in a village craves some Rava idli even though she has had Rava idli for the last 346514534 days in a row !! (Strange, you might think. But its normal down here)
# At the Idli shop there are two types of Rava Idli's available. One goes for Rs.A per piece and the other goes for Rs.B per piece. The girl has a total of K rupees.
# What is the maximum number of rava idlis that she can have?
# Note that she does not care about the type of idli she gets, she just wants to have as many rava idlis of any type as possible.
#   Input : The first line contains the number of test cases T
#           1 = T = 1000
#           Each test case contains three integers, A, B and K.
#           1 = A,B,K = 10^9
#   Output : Print the maximum number of idlis she can buy for each test case on a new line

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
