from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finances.db'
db = SQLAlchemy(app)

class Transaktion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<Transaktion {self.description} {self.amount}>'

@app.route('/api/import', methods=['POST'])
def import_data():
    if "file" not in request.files:
        return {"error": "No file part"}, 400
    file = request.files["file"]

    Transaktion.query.delete()
    db.session.commit()

    df = pd.read_excel(file, skiprows=8)

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
    return {"message": "Data imported successfully"}, 200



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/transactions')
def get_transactions():
    transactions = Transaktion.query.all()
    transaktioner = [
        {
            'id': tx.id,
            'date': tx.date,
            'description': tx.description,
            'amount': tx.amount,
            'type': tx.type
        } for tx in transactions
    ]
    return jsonify(transaktioner)

if __name__ == '__main__':
    app.run(debug=True)