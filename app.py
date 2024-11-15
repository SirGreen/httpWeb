from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    account = request.form.get('account')
    password = request.form.get('password')
    # Normally, you would validate the account and password here, but we're skipping this for the demo.
    return redirect(url_for('login_success'))

@app.route('/login-success')
def login_success():
    return "<h1>Login Successful</h1>"

if __name__ == '__main__':
    app.run(debug=True)
