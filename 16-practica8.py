tickets = [
    {
        "ticket_id": "INC2001",
        "vendor": "IZZI",
        "mttr": 5.5
    },
    {
        "ticket_id": "INC2002",
        "vendor": "Telmex",
        "mttr": 12.3
    },
    {
        "ticket_id": "INC2003",
        "vendor": "Megacable",
        "mttr": 8.7
    }
]

for ticket in tickets:
    print(ticket["ticket_id"])

for ticket in tickets:
    print(ticket["vendor"])

for ticket in tickets:
    if ticket["mttr"] > 10:
        print("High")
    else:
        print("Normal")
