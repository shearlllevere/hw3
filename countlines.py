userInput = raw_input("Please Enter a Filename: ")

afile = open("Input.txt",'r')

myFile = afile.read()

countlines = 0

for line in myFile:
	countlines +=1

print countlines
