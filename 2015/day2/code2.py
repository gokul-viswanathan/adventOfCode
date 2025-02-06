sum = 0
inputFile = open("input1.txt","r")
inputValues = inputFile.readlines()
inputFile.close()
for input in inputValues:
    #input = "2x3x4"
    z = input.split("x")
    l = int(z[0])
    b = int(z[1])
    h = int(z[2])
    values = [l,b,h]
    values.sort()
    ribbon = values.pop(0)*2 + values.pop(0)*2
    bow = l*b*h
    sum += (ribbon + bow)

print(sum)
