fname = input('Enter file: ')

try: fhandle = open(fname, 'r')
except:
	print('No such file.')
	quit()

emails = dict()
for line in fhandle:
	if not line.startswith('From '): continue
	line = line.split()
	email = line[1]
	i = email.find('@')
	email = email[i+1:]
	emails[email]=emails.get(email, 0) + 1

print(emails)
