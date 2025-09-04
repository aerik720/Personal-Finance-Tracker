import pandas as pd
from datetime import datetime
from Finances import db, app, Transaktion

# Läs Excel och hoppa över raderna innan rubrikerna
df = pd.read_excel("kontoutdrag.xlsx", skiprows=8)  


with app.app_context():
    for _, row in df.iterrows():
        date_obj = pd.to_datetime(row['Transaktionsdatum']).date()
        typec = 'credit' if float(row['Belopp']) > 0 else 'debit'
        tx = Transaktion(
            date=date_obj,
            description=str(row['Text']),
            amount=float(row['Belopp']),
            type=typec
        )
        db.session.add(tx)
    db.session.commit()
    print("Excel-data har lagts in i databasen!")

