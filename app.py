from flask import Flask,render_template

app = Flask(__name__) # Initialize the Flask application
@app.route('/') # Define the route for the root URL

def home():
    return render_template('index.html',name="piyush") # Return a simple greeting message

@app.route('/about')
def about():
    return render_template('about.html') # Return a simple about message

if __name__ == '__main__':
    app.run(debug=True) # Run the application in debug mode: