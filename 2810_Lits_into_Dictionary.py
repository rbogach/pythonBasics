
keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]

dic = {}
for key in keys:
	for value in values:
		dic[key] = value
		#values.remove(value)
		break

print("Dictionary: " + str(dic))
for value in dic.values():
	print(value[20])
