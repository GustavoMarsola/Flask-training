from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def initial_page():
    user = request.form.get('email')
    password = request.form.get('password')
    print(user,password)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
