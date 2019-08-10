import re

fname = input('Enter file name: ')

try:
        fhandle = open(fname, 'r')
except:
        print('No such file.')
        quit()

s = 0
cnt = 0
for line in fhandle:
    lst = re.findall('^New Revision: ([0-9]+)', line)
    cnt += len(lst)
    for item in lst:
        s += int(item)

print(s/cnt)
