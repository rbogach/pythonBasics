
hour = input("Please fill in the hour")
guard = True
if int(hour) < 17 and int(hour) >= 7:
    guard = False
    print("U are in")
else:
    print("U cant enter")