lst = list()

while True:
    txt = input('Enter a number: ')
    if txt == 'done': break
    
    try: nr = float(txt)
    except:
        print('Invalid input.')
        continue

    lst.append(nr)

print('Maximum:', max(lst))
print('Minimum:', min(lst))