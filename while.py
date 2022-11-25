bananas = input("Input your bananas")
bananas = int(bananas)
while bananas != 0:
    if bananas >= 5:
        print("I have a bunch of some 5 bananas")
        break
    elif bananas <= 4 and bananas >=1:
        print("I have a small bunch of some more than 1 -4 bananas")
        break
else:
    print("I have no bananas")