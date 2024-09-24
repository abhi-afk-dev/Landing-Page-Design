import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,timezone

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=f"sqlite:///{os.path.expanduser('~/downloads/hehe.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Data(db.Model):
    sno = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(100) , nullable =False)
    email = db.Column(db.String(100) , nullable =False)
    password = db.Column(db.String(15) , nullable =False)
    confirm_password = db.Column(db.String(15) , nullable =False)
    date_time = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self) -> str:
        return f"{self.sno} - {self.name} - {self.email}"
    

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/sign/', methods=['GET', 'POST'])
def sign():
    if request.method =='POST':
        name=request.form['name']
        email=request.form['inputEmail']
        password=request.form['inputPassword']
        confirmpassword=request.form['inputPassword']

        DATAS=Data(name=name,email=email,password=password,confirm_password=confirmpassword) 
        db.session.add(DATAS)
        db.session.commit()
        
    allcommit=Data.query.all
    return render_template('sign.html', allcommit=allcommit)



@app.route('/details/' , methods=['GET'])
def details():

    datas = Data.query.all()
    return render_template('details.html' , datas=datas)


if __name__ == '__main__':
    app.run(debug=True)

