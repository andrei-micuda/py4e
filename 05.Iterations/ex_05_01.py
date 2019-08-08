counter = 0
s = 0

while True:
    raw = input("Enter Number: ")
    if raw == "done":
        break

    try:
        n = float(raw)
    except:
        print("Invalid input.")
        continue

    s += n
    counter += 1


print(s, counter, s/counter)
