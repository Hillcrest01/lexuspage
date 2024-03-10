from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#we put our development database here
ENV= 'dev'

if ENV == 'dev':
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

else:
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

#The meaning of the line below to be researched later
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#here we now create the database object.
db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'Feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(30), unique=True)
    owner = db.Column(db.String(30))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    #we define a constructor for this class
    def __init__(self, customer, owner, rating, comments):
        self.customer = customer
        self.owner = owner
        self.rating = rating
        self.comments = comments
        
#this renders the index,html page
@app.route('/')
def index():
    return render_template('index.html')

#here we capture the form data using their names that were assigned in the html page then we render success.html page.
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        owner = request.form['owner']
        rating = request.form['rating']
        comments = request.form['comments']
        if customer == '' or owner == '':
            return render_template('index.html', message='Please enter the required fields')
        #print(customer, owner, rating, comments)

        return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)