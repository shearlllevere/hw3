L= []

while True:
	input = raw_input("Please input one number at a time: ")
	
	if input == "stop":
			break
	try:
		L.append(int(input))
	except:
		print('Max Integer')
		break

print(max(L))   
