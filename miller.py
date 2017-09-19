import random

def miller_rabin(n, k=10):
    # from github.com/bnlucas/miller_rabin.py
    if n == 2:
        return True
    if not n & 1:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in xrange(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in xrange(k):
        a = random.randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True

f = open("minNum.txt", "r")
minIter = long(f.read())

g = open("maxNum.txt", "r")
maxIter = long(g.read())

g = open("baseNum2.txt", "r")
# baseNum = long(g.read())
baseNum = g.read()

i = minIter + 1
while i < maxIter:
    num = long(baseNum + str(i))

    if miller_rabin(num):
        print "**** POTENTIAL PRIME ****"
        print num

    i += 2



