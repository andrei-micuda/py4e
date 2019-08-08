fname = input('Enter file name: ')

try: fhandle = open(fname, 'r')
except:
        print('No such file.')
        quit()

words = list()
for line in fhandle:
        parts = line.split()
        for word in parts:
                if word not in words:
                        words.append(word)

words.sort()
print(words)
