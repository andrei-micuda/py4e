fname = input('Enter file: ')

try:
    fhandle = open(fname, 'r')
except:
    print('No such file.')
    quit()

hrs = dict()
for line in fhandle:
    if not line.startswith('From '):
        continue

    tmp = line.find(':')
    hour = line[tmp-2:tmp]
    hrs[hour] = hrs.get(hour, 0) + 1

for (k, v) in sorted(hrs.items()):
    print(k, v)
