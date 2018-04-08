from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('user_signon.html')

@app.route("/user-input", methods=['POST'])
def user_input():
    namein = request.form['username']
    pwin = request.form['password']
    vpwin = request.form['verify']
    emin = request.form['email']
    namein_error = ""
    pwin_error = ""
    vpwin_error = ""
    emin_error = ""

    if namein:
        if " " in namein:
            namein_error = "Username cannot contain spaces"    
        else:
            if len(namein) < 3 or len(namein) > 20:
                namein_error = "Username must be between 3 and 20 characters in length"
    else:
        namein_error = "Username cannot be empty"

    if pwin:
        if " " in pwin:
            pwin_error = "Password cannot contain spaces"    
        else:
            if len(pwin) < 3 or len(pwin) > 20:
                pwin_error = "Password must be between 3 and 20 characters in length"
    else:
        pwin_error = "Password cannot be empty"

    if vpwin:
        if vpwin != pwin:
           vpwin_error = "Passowrds do not match, Please re-enter matching passwords"

    else:
        vpwin_error = "Verification password cannot be empty"

    if emin:
        emerror_flag = False
        if emin.count("@") != 1: 
            emerror_flag = True

        if emin.count(".") != 1:
            emerror_flag = True

        if " " in emin:
            emerror_flag = True

        if (len(emin) < 3 or len(emin) > 20):
            emerror_flag = True

        if emerror_flag == True:
            emin_error = "Invalid email address.  Please enter a valid email address"
    
    if namein_error or pwin_error or vpwin_error or emin_error:
        return render_template("user_signon.html", un_1=namein, un_p=namein_error,
        pw_p=pwin_error, vpw_p=vpwin_error, em_1=emin, em_p=emin_error)
    else:
        return render_template('welcome.html', name=namein)
    #return "hey"

app.run()