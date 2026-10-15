mttr = 8

if mttr <= 6:
    print("Within SLA")
elif mttr <= 10:
    print("Warning")
else:
    print("Breached")