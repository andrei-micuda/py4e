def computepay(hrs, rate):
    if hrs <= 40:
        pay = hrs*rate
    else:
        pay = 40*rate
        pay += (hrs-40)*rate*1.5
    return pay


h = int(input("Enter Hours: "))
r = float(input("Enter Rate: "))

pay = computepay(h, r)

print(pay)
