# imports render_template from Flask to render templates
from flask import Flask, render_template, request

"""
    All templates are stored in the 'templates' directory. 
    This is standard for Flask applications.
"""
app = Flask(__name__)

# Define the home route "[ip-adress]:5000". A name can be passed as a query parameter named 'name'.
# Vad händer ifall man skriver t.ex. "localhost:5000?name=Holger" i webbläsaren?
@app.route('/')
def home():
    if not request.args.get('name'):
        name = "World"
    else:
        name = request.args.get('name')
    # Render the index.html template with a name variable
    return render_template('index.html', name=name)

@app.route('/lararlista')
@app.route('/sneakers')
def lararlista():
    subjects = [
        {'amne': 'Matematik', 'elever': 28, 'larare': 'Anna Svensson'},
        {'amne': 'Svenska', 'elever': 24, 'larare': 'Erik Karlsson'},
        {'amne': 'Engelska', 'elever': 26, 'larare': 'Sofia Nilsson'},
        {'amne': 'Historia', 'elever': 22, 'larare': 'Jonas Berg'}
    ]
    return render_template('sneakers.html', subjects=subjects)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')