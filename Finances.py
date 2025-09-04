from datetime import datetime
import Konto as K
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

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