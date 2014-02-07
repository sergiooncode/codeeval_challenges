import sys

def onescounter(t):
	if t == 0: 
		return 0
	if t == 1:
		return 1
	abovepow = 1
	oc = 0
	while abovepow < t:
	    abovepow = abovepow*2
	b = abovepow / 2
	s = b
	oc = oc + 1
	while s != t:
		if s + b / 2 <= t:
		    s = s + b / 2
		    oc = oc + 1
		    b = b / 2 
		else:
			b = b / 2
	return oc

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    if test not in ['\n', '\n\r']:
    	print 'next test is: ' + test 
    	print str(onescounter(int(test)))

test_cases.close()

