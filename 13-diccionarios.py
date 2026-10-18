ticket = {
    "ticket_id": "INC1001",
    "vendor": "Telmex",
    "prioridad": "P1",
    "estado": "Cerrado",
    "mttr": 3.5
}

print(ticket["ticket_id"])
print(ticket["vendor"])
print(ticket["mttr"])

if ticket["mttr"] > 10:
    print("High")
else:
    print("Normal")