mn = None
mx = None

while True:
    raw = input("Enter Number: ")
    if raw == "done":
        break
    try:
        n = int(raw)
    except:
        print("Invalid input")
        continue

    if mn is None:
        mn = n
    elif n < mn:
        mn = n

    if mx is None:
        mx = n
    elif n > mx:
        mx = n

print("Maximum is", mx)
print("Minimum is", mn)
