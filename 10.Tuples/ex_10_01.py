fname = input('Enter file: ')

try:
    fhandle = open(fname, 'r')
except:
    print('No such file.')
    quit()

emails = dict()
for line in fhandle:
    if not line.startswith('From '):
        continue

    words = line.split()
    emails[words[1]] = emails.get(words[1], 0) + 1

tmp = list()
for (k, v) in emails.items():
    tmp.append((v, k))

tmp = sorted(tmp, reverse = True)

for (v, k) in tmp[:1]:
    print(k, v)
