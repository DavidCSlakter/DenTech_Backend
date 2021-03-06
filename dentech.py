from flask import Flask, request, session, url_for, redirect
app = Flask(__name__)

#Authenticates the login
@app.route('/webapp/loginAuth', methods=['GET', 'POST'])
def loginAuth():
    data = request.data
    return 'dashboard.html'

    # if(data):
    #     #creates a session for the the user
    #     #session is a built in
    #     session['username'] = username
    #     return redirect(url_for('home'))
    # else:
    #     #returns an error message to the html page
    #     error = 'Invalid login or username'
    #     return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run('127.0.0.1', 5000)