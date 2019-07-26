fname = input('Enter file name: ')

try: fhandle = open(fname, 'r')
except:
    print('No such file.')
    quit()

counter = 0
for line in fhandle:
    if not line.startswith('From '):
        continue

    counter += 1
    words = line.split()
    print(words[1])

print('There were', counter, 'lines in the file with From as the first word')
