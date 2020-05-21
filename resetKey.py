import random
import string
import pickle

def randomString(stringLength=8):
    stringCharacter = string.ascii_uppercase + string.digits
    return ''.join(random.choice(stringCharacter) for i in range(stringLength))

a = randomString()
b = randomString()
c = randomString()
d = randomString()
e = randomString()
f = randomString()
g = randomString()
h = randomString()
i = randomString()
j = randomString()
k = randomString()
l = randomString()
m = randomString()
n = randomString()
o = randomString()
p = randomString()
q = randomString()
r = randomString()
s = randomString()
t = randomString()
u = randomString()
v = randomString()
w = randomString()
x = randomString()
y = randomString()
z = randomString()
space = randomString()
comma = randomString()
period = randomString()
keyList = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, space, comma, period]

with open('key.pkl', 'wb') as f:
    pickle.dump(keyList, f)

print('Success')
