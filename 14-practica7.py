ticket = {
    "ticket_id": "INC2001",
    "vendor": "IZZI",
    "prioridad": "P2",
    "estado": "Abierto",
    "mttr": 11.5
}

print(ticket["ticket_id"])
print(ticket["vendor"])
print(ticket["mttr"])
ticket["estado"] = "cerrado"

if ticket["mttr"] > 10:
    print("High")
else: 
    print("Normal")