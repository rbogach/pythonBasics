n = input("Enter Number")
n = int(n)
totalNo = n
sum = 0
while (n > -1):
    sum += n
    n -= 1
    #totalNo +=n

average = sum / totalNo
print("average of", totalNo, "using while loop ", average)