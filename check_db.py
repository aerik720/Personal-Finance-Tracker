from Finances import db, app
from Finances import Transaktion  # om du lagt modellen i models.py, annars importera rätt

with app.app_context():
    rows = Transaktion.query.limit(20).all()
    for row in rows:
        print(row.id, row.date, row.description, row.amount, row.type)
