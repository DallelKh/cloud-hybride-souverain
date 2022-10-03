from crypt import methods
from email.policy import default
from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:root@db-6cf6d555ff-tp7m5:5432/pass_culture'

db=SQLAlchemy(app)
class Beneficiaire(db.Model):
    __tablename__='beneficiaire'
    id=db.Column(db.Integer,primary_key=True)
    fname=db.Column(db.String(40))
    lname=db.Column(db.String(40))
    dateOfBirth= db.Column(db.DateTime,nullable=False)
    addresse=db.Column(db.String(40))

    def __init__(self,fname,lname,dateOfBirth,addresse):
      self.fname=fname
      self.lname=lname
      self.dateOfBirth=dateOfBirth
      self.addresse=addresse

    def __repr__(self) -> str:
       return super().__repr__()

class Offre(db.Model):
    __tablename__='offre'
    id=db.Column(db.Integer,primary_key=True)
class Fournissseur(db.Model):
    __tablename__='fournisseur'
    id=db.Column(db.Integer,primary_key=True)
class Coord_fournisseur(db.Model):
    __tablename__='coord_fournisseur'
    id=db.Column(db.Integer,primary_key=True)
class idJustificatifIdentite(db.Model):
    __tablename__='idJustificatifIdentite'
    id=db.Column(db.Integer,primary_key=True)

class Reservation(db.Model):
    __tablename__='reservation'
    id=db.Column(db.Integer,primary_key=True)

class Inventaire(db.Model):
    __tablename__='inventaire'
    id=db.Column(db.Integer,primary_key=True)

class Transaction(db.Model):
    __tablename__='transaction'
    id=db.Column(db.Integer,primary_key=True)

class SensibilityLevel(db.Model):
    __tablename__='sensibilityLevel'
    id=db.Column(db.Integer,primary_key=True)

class Preferences(db.Model):
    __tablename__='preferences'
    id=db.Column(db.Integer,primary_key=True)

  

@app.route('/')
def home():
    db.create_all()
    return render_template("form.html")

#post
@app.route('/submit', methods=['GET','POST'])
def submit():

  if request.method=='POST':
  
     fname= request.form['fname']
     lname=request.form['lname']
     addresse=request.form['addresse']
     dateOfBirth=request.form['dateOfBirth']

     beneficiaire=Beneficiaire(fname,lname,dateOfBirth,addresse)
     db.session.add(beneficiaire)
     db.session.commit()

  #fetch a certain beneficiaire
  beneficiaireResult=db.session.query(Beneficiaire).filter(Beneficiaire.id==1)
  for result in beneficiaireResult:
    print(result.fname)

  return render_template('home.html', data=fname)
#get
@app.route('/offres/<id>', methods=['GET'])
def get_offre(id):
  offre=Offre.query.filter_by(id=id).one()
  formatted_offre=format(offre)
  return {'offre':formatted_offre}

#delete
@app.route('/offres/<id>', methods=['DELETE'])
def DELETE_offre(id):
  offre=Offre.query.filter_by(id=id).one()
  db.session.delete(offre)
  db.session.commit()
  return {'offre (id: {id})deleted successfully!'}

#edit 
@app.route('/offres/<id>', methods=['PUT'])
def update_offre(id):
  offre=Offre.query.filter_by(id=id)
  #offre2=request.form[]
  offre.update()
  db.session.delete(offre)
  db.session.commit()
  return {'offre (id: {id})deleted successfully!'}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True) #debug is on so that code changes are directly applied even when running app
