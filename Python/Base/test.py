from math import sqrt
for n in range(99,0,-1):
    root = sqrt(n)
    if root == int(root):
        print n
        continue
    else:
        print "didn't find it"