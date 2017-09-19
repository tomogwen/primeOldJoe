import numpy as np
np.set_printoptions(threshold=np.nan)

img = open("oldJoeHalf.bmp", "r")
img = list(img.read())
num = []

for i in range(len(img))[54:]:
    if img[i] == '\x00':
        num.append(0)
    elif img[i] == '\xff':
        num.append(1)
    else:
        num.append(9)

number = int(''.join(map(str,num)))
numSplit = []

for i in range(0, len(num)-3, 4):
    numSplit.append("{0}{1}{2}{3}".format(num[i], num[i+1], num[i+2], num[i+3]))

finalNum = []
for i in range(len(numSplit)):
    if numSplit[i] == '0001':
        finalNum.append(1)
    elif numSplit[i] == '1111':
        finalNum.append(8)

print finalNum
print int(''.join(map(str,finalNum)))
print len(finalNum)


# numArray =  np.reshape(num, (50,152))
# actual image is 25 * 76
# array format is 50 * 152
