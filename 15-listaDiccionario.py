tickets = [
    {
        "ticket_id": "INC1001",
        "vendor": "Telmex",
        "mttr": 3.5
    },
    {
        "ticket_id": "INC1002",
        "vendor": "IZZI",
        "mttr": 11.3
    },
    {
        "ticket_id": "INC1003",
        "vendor": "Totalplay",
        "mttr": 7.2
    }
]

for ticket in tickets:
    print(ticket)

for ticket in tickets:
    print(ticket["vendor"])


for ticket in tickets:
    print(ticket["mttr"])


for ticket in tickets:
    if ticket["mttr"] > 10:
        print("High")
    else:
        print("Normal")


for ticket in tickets:
    if ticket["mttr"] > 10:
        print(ticket["ticket_id"], "High")
    else:
        print(ticket["ticket_id"], "Normal")