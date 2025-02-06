
a = []
b = []
with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        lineOut = line.split()
        if lineOut != []:
            a.append(int(lineOut[0]))
            b.append(int(lineOut[1]))

a.sort()
b.sort()
output = 0
for i in range(len(a)):
    output += abs(a[i] - b[i])
print(output)
