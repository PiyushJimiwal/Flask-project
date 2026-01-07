from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__) # Initialize the Flask application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db' # Configure the database URI
db = SQLAlchemy(app) # Initialize the SQLAlchemy object

class User(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    username  = db.Column(db.String(80),nullable=False)
    password = db.Column(db.String(200),nullable=False)
    datetime = db.Column(db.DateTime,default=datetime.utcnow)

with app.app_context():
    db.create_all() # Create the database tables

@app.route('/') # Define the route for the root URL
def home():
    all_user = User.query.all() # Query all users from the database
    return render_template('index.html', all_user=all_user) # Return a simple greeting message

@app.route('/about')
def about():
    return render_template('about.html') # Return a simple about message

@app.route('/login',methods =['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = User(
            username=username, 
            password=password
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect('/')
        print(f"Username: {username}")
        print(f"Password: {password}")
        # Here you would typically validate the username and password
        return render_template('login.html', username=username)
    return render_template('login.html') # Return a simple login message

@app.route('/update/<int:sno>',methods = ['GET','POST'])
def update(sno):
    user = User.query.filter_by(sno=sno).first()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user.username = username
        user.password = password
        db.session.commit()
        return redirect('/')
    return render_template('update.html',user=user)

@app.route('/delete/<int:sno>')
def delete(sno):
    user = User.query.filter_by(sno=sno).first()
    db.session.delete(user)
    db.session.commit() 
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True) # Run the application in debug mode: