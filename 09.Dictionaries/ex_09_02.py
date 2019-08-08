fname = input('Enter file: ')

try: fhandle = open(fname, 'r')
except:
    print('No such file.')
    quit()

days = dict()
for line in fhandle:
    if not line.startswith('From'): continue
    words = line.split()
    if len(words) < 3: continue
    day = words[2]
    days[day] = days.get(day, 0) + 1

print(days)
