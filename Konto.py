import json
from datetime import datetime

json_fil = 'Kontoutdrag.json'

with open(json_fil, 'r', encoding='utf-8') as f:
    data = json.load(f)

Total = data['transactions'][-1]['balance']

def Yinkomst(data, år=2025):
    Ytotal = 0
    for tx in data['transactions']:
        if tx['type'] == 'credit' and datetime.strptime(tx['date'], '%Y-%m-%d').year == år:
            Ytotal += tx['amount']
    print(f"Totala inkomster för {år}: {Ytotal} kr")

def Yutgift(data, år=2025):
    Ytotal = 0
    for tx in data['transactions']:
        if tx['type'] == 'debit' and datetime.strptime(tx['date'], '%Y-%m-%d').year == år:
            Ytotal += tx['amount']
    print(f"Totala utgifter för {år}: {Ytotal} kr")