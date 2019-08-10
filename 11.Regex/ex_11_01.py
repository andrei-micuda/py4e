import re

fname = input('Enter file name: ')
try:
        fhandle = open(fname, 'r')
except:
        print('No such file.')
        quit()

regex = input('Enter a regular expression: ')

s = 0
for line in fhandle:
        if re.search(regex, line): s += 1

print(fname, 'had', s, 'lines that matched', regex)
