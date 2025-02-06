inputFile = open("input1.txt","r")
data = inputFile.read()
inputFile.close()
#data = ")" counter = 0
openCounter = 0
closeCounter = 0
for pos,i in enumerate(data):
    if i == "(":
        counter += 1
        openCounter += 1
    else:
        counter -= 1
        closeCounter += 1
    if counter == -1:
        print("pos is : ",pos+1)
        break
print(counter, openCounter, closeCounter)
