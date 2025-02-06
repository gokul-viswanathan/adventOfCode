"""
2x3x4 requires 2*6 + 2*12 + 2*8 = 52
20x3x11
"""
sum = 0
inputFile = open("input1.txt")
inputvalues = inputFile.readlines()
inputFile.close()

for input in inputvalues:
    #input = "2x3x4"
    z = input.split("x")
    print(z)
    lw = int(z[0])*int(z[1])
    wh = int(z[1])*int(z[2])
    hl = int(z[2])*int(z[0])
    sum += 2*lw + 2*wh + 2*hl + min(lw,wh,hl)
    print(sum)
print(sum)


