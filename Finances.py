import json
from datetime import datetime
import Konto as K
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finances.db'
db = SQLAlchemy(app)

class Översikt(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f'<Översikt {self.id}>'

@app.route('/')
def index():
    return render_template('index.html')


#år = int(input("Ange år: "))
#K.Yinkomst(K.data, år)

if __name__ == '__main__':
    app.run(debug=True)