import os, sys

key=sys.argv[1]
if len (key) != 1201:
	sys.exit (0)
index = 1
s=key
while index < len (s) :
	print "checking index = %s" % (index, )
	x0 = s[0:-index]
	x1 = s[index:]
	xx0 = [x for x in x0]
	xx1 = [x for x in x1]
	xx0 = map (lambda t : int (t), xx0)
	xx1 = map (lambda t : int (t), xx1)
	yy = zip (xx0, xx1)
	yy = map (lambda t : t[0] * t[1], yy)
	yy = reduce (lambda a, b : a ^ b, yy)

	index = index + 1

	if yy == 1:
		continue
	else:
		print "fail\n"
		sys.exit (0)

print "Win!"

