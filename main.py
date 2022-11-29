from flask import Flask, render_template, request, redirect, url_for, abort
from connection import Database

app = Flask(__name__)
db = Database()

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('email')
        password = request.form.get('password')
        verify = db.compare(user,password)
        if verify is True:
            return redirect(url_for('initial_page'), code=302)
        else: 
            abort(401)
    return render_template('login.html')

@app.route('/initial_page')
def initial_page():
    return render_template('initial_page.html')

if __name__ == '__main__':
    app.run(debug = True)
