from flask import render_template
from app import app
""" 
    handlers for the application routes/view functions.
    @app.route decorator creates an association between the URL given as an argument and the function

    Returns:
        string Hello Africa
    """
@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Sindani'}
    """mock object: creating object user that doesn't exist
        for testing purpose
    """
    return render_template('index.html', title='Home', user=user)
    # return render_template('index.html', user=user)
    # if title is not defined, jinja replaces with else statement content
    # for title in routes.py
    