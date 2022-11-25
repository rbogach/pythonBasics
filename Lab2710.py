isBreak = False
thenumbers = []
while not isBreak:
    number = input("Please input the number")
    try:
        number = int(number)
    except ValueError:
        print("Please enter Integer")
    if number >= 0:
        thenumbers.append(number)
        continue
    else:
        average = float(sum(thenumbers)) / float(len(thenumbers))
        print(average)
        isBreak = True
