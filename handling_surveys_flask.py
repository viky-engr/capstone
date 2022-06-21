#receive form data from website
#from https://developer.mozilla.org/en-US/docs/Learn/Forms/Sending_and_retrieving_form_data 
#install flask https://flask.palletsprojects.com/en/2.1.x/quickstart/#static-files 
#https://overiq.com/flask-101/form-handling-in-flask/
#to run this code locally you'll need to install Python/PIP, then install Flask using pip3 install flask. 
#At this point you should be able to run the example using python3 python-example.py, then navigating to localhost:5042 in your browser.

from flask import Flask, render_template, request
#...
#app = Flask(__name__)

@app.route('/form/', methods=['get', 'post'])
def form():
    if request.method == 'post':
        sex = request.form.get('Sex') #access data in form
        
        if sex='M' or 'F' or 'X':
        message = "submitted successfully"
        else
        message = "invalid input"
        
    return render_template('form.html', message=message)
#...