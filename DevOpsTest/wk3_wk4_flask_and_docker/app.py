from flask import Flask, request, render_template, Response, url_for
from werkzeug.utils import secure_filename, redirect

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/abc')
def abc():
    return 'Hello abc'


@app.route('/upload')
def upload():
    return render_template('upload.html')


@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('uploaded_files/' + secure_filename(f.filename))
        return Response("file uploaded successfully", status=201)

# Redirect
@app.route('/secrets')
def secrets():
    token = request.cookies.get('token')
    if not token or token != USERNAME + PASSWORD:
        return redirect(url_for('login'))
    return Response("The secret is you have successfully set the token via cookie when you login\n")


USERNAME = 'admin'
PASSWORD = 'admin'


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != USERNAME or request.form['password'] != PASSWORD:
            error = 'Invalid Credentials. Please try again.'
        else:
            response = redirect(url_for('secrets'))
            response.set_cookie("token", USERNAME + PASSWORD)
            return response
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True)
