import os
from flask import Flask, flash, request, redirect, url_for, render_template, make_response, abort, session
from werkzeug.utils import secure_filename
from markupsafe import escape

UPLOAD_FOLDER = 'uploaded_file'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'jpg', 'png'}



app = Flask(__name__)
app.secret_key = "super confidential key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def hello_world():
    return """<p>Hello there! Welcome to this simple project</p>
            <a href='/test'> Click here to go to test page </a>
            <p> <a href='/login'> Login </a> </p>
            <p> <a href='/setcookies'> Set Cookies </a>"""

@app.route("/test")
def test_page():
    return "<h1>This is the testing page!</h1>"

@app.route('/user/<username>')
def user_profile(username):
    return f'This is your profile: {escape(username)}' 

@app.route('/post/<int:car_id>')
def show_car(car_id):
    return f'Car: {car_id}'

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session['user'] = request.form['user']
        
        return redirect(url_for('user_landing'))
    else:
        return render_template("login.html")

@app.route('/user_landing')
def user_landing():
    if 'user' in session:
        return f''' Logged in as <h3>{session["user"]}</h3>

        <p>Click here to upload some files</p>
        <a href='/upload'> Upload file </a>
        
        <a href="/logout"> Log out </a>
        '''  
    return """ 
        <p>You are currently not logged in <a href='/login'> Click here to login </a> </p>
        """


def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload' , methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        #to check if the POST request have content of the file
        if 'file' not in request.files:
            flash('No file available')
            return redirect(request.url)
        file = request.files['file']
        #if file is emply, browser submits empty file without filename
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            #to get the name of the file that is uploaded from user
            filename = secure_filename(file.filename)
            #to save the uploaded image in the specified folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_success', name=filename))
    return render_template('upload.html')

@app.route('/upload_success')
def upload_success():
    return '<h1> Upload is successful'


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('hello_world'))        

@app.route('/cookies')
def cookies():
    username=request.cookies.get('username')
    return f"""<h1>Your cookie is: {username} </h1>
            <p>The cookie has been set and can be displayed</p>
    """

@app.route('/setcookies')
def setcookies():
    resp = make_response(render_template('set_cookie.html'))
    resp.set_cookie('username', 'Azhad')
    return resp


if __name__ == '__main__':
    
    app.config['SESSION_TYPE'] = 'filesystem'

    app.debug = True
    app.run()
