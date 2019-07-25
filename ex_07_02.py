fname = input('Enter file name: ')

try:
    fhandle = open(fname, 'r')
except:
    print('No such file.')
    quit()

s = 0
count = 0
for line in fhandle:
    line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:'):
        continue

    colon_pos = line.find(':')
    s += float(line[colon_pos+2:])
    count += 1

print('Average spam confidence:', s/count)
