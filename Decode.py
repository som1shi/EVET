import random
import string
import pickle

f = open('key.pkl', 'rb')
keyList = pickle.load(f)
f.close()


line = str(input('What is the message you want to decode? '))


line = line.replace(keyList[0], 'a')

line = line.replace(keyList[1], 'b')

line = line.replace(keyList[2], 'c')

line = line.replace(keyList[3], 'd')

line = line.replace(keyList[4], 'e')

line = line.replace(keyList[5], 'f')

line = line.replace(keyList[6], 'g')

line = line.replace(keyList[7], 'h')

line = line.replace(keyList[8], 'i')

line = line.replace(keyList[9], 'j')

line = line.replace(keyList[10], 'k')

line = line.replace(keyList[11], 'l')

line = line.replace(keyList[12], 'm')

line = line.replace(keyList[13], 'n')

line = line.replace(keyList[14], 'o')

line = line.replace(keyList[15], 'p')

line = line.replace(keyList[16], 'q')

line = line.replace(keyList[17], 'r')

line = line.replace(keyList[18], 's')

line = line.replace(keyList[19], 't')

line = line.replace(keyList[20], 'u')

line = line.replace(keyList[21], 'v')

line = line.replace(keyList[22], 'w')

line = line.replace(keyList[23], 'x')

line = line.replace(keyList[24], 'y')

line = line.replace(keyList[25], 'z')

line = line.replace(keyList[26], ' ')

line = line.replace(keyList[27], ',')

line = line.replace(keyList[28], '.')

print (line)
