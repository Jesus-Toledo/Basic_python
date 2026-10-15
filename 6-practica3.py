mttr_promedio = 7.8
mttr_status = ""

if mttr_promedio <=  6:
    mttr_status = "Within SLA"
elif mttr_promedio <= 10:
    mttr_status = "Warning"
else:
    mttr_status = "Breached"

print(mttr_status)

