fname = input('Enter file: ')

try:
    fhandle = open(fname, 'r')
except:
    print('No such file.')
    quit()

letters = dict()
for line in fhandle:
    line = line.lower()
    for char in line:
        if not char.isalpha():
            continue
        
        letters[char] = letters.get(char, 0) + 1
 
tmp = sorted([(v, k) for (k, v) in letters.items()], reverse = True)

for (freq, ltr) in tmp:
    print(ltr, freq)
