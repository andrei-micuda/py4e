fname = input('Enter file name: ')
if fname == 'na na boo boo': print('NA NA BOO BOO TO YOU - You have been punk\'d!')
else:
    try: fhandle = open(fname, 'r')
    except:
        print('No such file.')
        quit()

    counter = 0
    for line in fhandle:
        counter += 1

    print('There were', counter, 'subject lines in', fname)
