def computegrade(score):
    if score>=0.0 and score<=1.0:
        if score>=0.9: return 'A'
        elif score>=0.8: return 'B'
        elif score>=0.7: return 'C'
        elif score>=0.6: return 'D'
        else: return 'F'
    else: return 'Score not in range 0.0-1.0.'

val = float(input("Enter Score: "))

print(computegrade(val))
