lines = [line.rstrip('\n') for line in open('test.txt')]
print lines

print type(lines)

line1 = len(lines[0])
print lines[0],'\n', type(lines[0])
print 'first line length', line1

print lines[0][line1-1]

line2 = len(lines[1])
print 'second line length ', line2


print "printing last element, if clear is white character such as space or '\n'",lines[1][line2-1]
