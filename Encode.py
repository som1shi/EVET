import random
import string
import pickle

f = open('key.pkl', 'rb')
keyList = pickle.load(f)
f.close()



line = str(input('What message is to be encoded? '))


line = line.replace('a', keyList[0])

line = line.replace('b', keyList[1])

line = line.replace('c', keyList[2])

line = line.replace('d', keyList[3])

line = line.replace('e', keyList[4])

line = line.replace('f', keyList[5])

line = line.replace('g', keyList[6])

line = line.replace('h', keyList[7])

line = line.replace('i', keyList[8])

line = line.replace('j', keyList[9])

line = line.replace('k', keyList[10])

line = line.replace('l', keyList[11])

line = line.replace('m', keyList[12])

line = line.replace('n', keyList[13])

line = line.replace('o', keyList[14])

line = line.replace('p', keyList[15])

line = line.replace('q', keyList[16])

line = line.replace('r', keyList[17])

line = line.replace('s', keyList[18])

line = line.replace('t', keyList[19])

line = line.replace('u', keyList[20])

line = line.replace('v', keyList[21])

line = line.replace('w', keyList[22])

line = line.replace('x', keyList[23])

line = line.replace('y', keyList[24])

line = line.replace('z', keyList[25])

line = line.replace(' ', keyList[26])

line = line.replace(',', keyList[27])

line = line.replace('.', keyList[28])

print (line)
