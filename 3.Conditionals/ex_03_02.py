try: hrs = int(input("Enter Hours: "))
except:
    print('Error, please enter numeric input')
    quit()
try: rate = float(input("Enter Rate: "))
except:
    print('Error, please enter numeric input')
    quit()
pay = 0

if hrs > 40 :
    rem_hrs = hrs - 40
    pay = pay + rem_hrs*1.5*rate

pay = pay+40*rate

print(pay)
