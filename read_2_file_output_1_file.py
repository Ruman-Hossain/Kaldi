o = open('output.txt', 'wb')

fh = open('input.txt', 'rb')
fh2 = open('input2.txt', 'rb')

for line in fh.readlines():
    o.write(line.strip('\r\n') + '\t' + fh2.readline().strip('\r\n') + '\n')