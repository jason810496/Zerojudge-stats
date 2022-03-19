from flask import Flask, redirect, url_for, render_template,request,flash , send_file

from flask_login import LoginManager , login_user, current_user, logout_user , UserMixin

from ZJquery import ZJ

from datetime import timedelta

from Theme import *

# Heroku branch 

# last update 3/1 10:57 am 
'''
from pathlib import Path

from bs4 import BeautifulSoup as bs
import re

import json
import requests as req
'''

Theme.Init()

app = Flask(__name__)
app.config['DEBUG'] = False
app.config['SECRET_KEY'] = 'My super secret key'
#app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

app.permanent_session_lifetime = timedelta( minutes=30 )

login_manager = LoginManager()
login_manager.init_app(app)

Admin = {
	"COOKIEID" : "Current logged in Zerojudge account cookieID",
	"USR" : "admin user name",
	"PWD" : "admin user password"
}


class User(UserMixin): 
	pass
	
@login_manager.user_loader  
def user_loader(usr_id):  

	user = User()  
	user.id = usr_id 
	return user  
    
@app.route("/")
def hello_world():
    return render_template("index.html")
    
@app.route("/login" , methods=["GET" , "POST"])
def login():
	if request.method == "POST" :
		usr = request.form["usr"]
		pwd = request.form["pwd"]	
		
		if usr==Admin["USR"] :
			
			if pwd==Admin["PWD"] :
			
				user = User()
				user.id = hash(usr+pwd)
				
				login_user( user )
				flash( "logged in successfully!" , category="success")
				
				return redirect( url_for("admin") )
			else :
				flash("Incorrect password !", category="danger")
				
				return render_template("login.html" , error="Incorrect password!")
		else:
			flash("User not existed!" , category="danger")
			return render_template("login.html" , error="User not existed !")
	else:
		
		if current_user.is_active: 
			return redirect( url_for("admin") )
			
		return render_template("login.html")


@app.route("/logout")
def logout():
	logout_user()
	flash("Successfully logout ! ",'success')
	return redirect(url_for('login'))
	
@app.route("/user" , methods=['GET'])
def Get_User():
	args =  request.args
	
	Name = args.get("name" , default="User", type=str)
	user_id = args.get("user_id" , type=str)
	theme_name   = args.get("theme" , default="default", type=str)
	T={}
	if theme_name in Theme.THEME_DIC:
		T=Theme.THEME_DIC[ theme_name ]
	else:
		T=Theme.THEME_DIC['default']
	
	if ZJ.Is_Connect():
		Data = ZJ.query(user_id)

		if Data:
			return app.response_class( render_template("img.svg" , 
				AC_TIME = Data['AC'],
				WA_TIME = Data['WA'],
				TLE_TIME = Data['TLE'],
				Total = int(Data['Total'] ),
				User = Name,
				Theme = T
			) , mimetype='image/svg+xml' )

		else:# user not found 
			return app.response_class( render_template("404.svg") , mimetype='image/svg+xml' )
	
	return app.response_class( render_template("500.svg") , mimetype='image/svg+xml' )


@app.route("/admin", methods=['GET','POST'] )
def admin():
 
	if request.method == "POST" :
	
		if request.form.get('change') == 'Change': 
			Admin["COOKIEID"] = request.form["cookie"]
			# flash("Update new ZJ Cookie", category="success")

			ZJ.Update_Cookie( Admin["COOKIEID"] )

			if ZJ.Is_Connect():
				flash("Login to ZJ successfully", category="success")
				return render_template("admin.html")
			else:
				flash("Fail to login to ZJ ", category="danger")
				return render_template("admin.html")
					
		elif request.form.get('check') == 'Check': 
	
			if ZJ.Is_Connect() :
				flash("Connect to ZJ successfully !", category="success")
				return render_template("admin.html")
			else:
				flash("Fail to connect to ZJ !", category="danger")
				return render_template("admin.html" )
				
		
	else :
		if current_user.is_active: 
			return render_template("admin.html")
		else:
			return redirect( url_for('login') )	

if __name__  ==  '__main__' :

	app.run( threaded=True, port=5000 )
	
	

	
    
    
    
    
