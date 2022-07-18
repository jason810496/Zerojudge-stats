from flask import Flask, redirect, url_for, render_template,request,flash , send_file

from Theme import *

import requests as req

ZJTotal = 2850
Theme.Init()

app = Flask(__name__)
app.config['DEBUG'] = False
app.config['SECRET_KEY'] = "104c5bdbefc64c7690b2a9e6ee59c703"

Admin = {
	"USR" : "zjquery01",
	"PWD" : "==+ZJquery424+=="
}

    
@app.route("/" , methods=["GET"])
def homePage():
	theme_name = request.args.get("theme" , default="nord", type=str)
	print( theme_name )

	return render_template("index.html" , themeName=theme_name, ThemeDictionary=Theme.THEME_DIC , 
			AC_TIME = 500,
			WA_TIME = 123,
			TLE_TIME = 99,
			Total = int( 100*500/ZJTotal ),
			User = "User",
			Theme = Theme.THEME_DIC[ theme_name] )
 
@app.route("/user" , methods=['GET','POST'])
def Get_User():
	args =  request.args
	
	# required arguments 

	Accout = args.get("account" , default="" , type=str )
	Name = args.get("name" , default="User", type=str)
	theme_name = args.get("theme" , default="nord", type=str)

	# optional arguments

	height = args.get("height" , default="250px" , type=str )
	width = args.get("width" , default="400px" , type=str )
	border = args.get("border" , default="none" , type=str )

	T={}
	
	if theme_name in Theme.THEME_DIC:
		T=Theme.THEME_DIC[ theme_name ]
	else:
		T=Theme.THEME_DIC['default']
	
	url = "https://zerojudge.tw//User/V1.0/Accepted?account=" + Accout
	respondJson = req.get( url ).json()

	if respondJson['userid'] : # user existed
		Accepted = len(respondJson['accepted'])
		return app.response_class( render_template("img.svg" , 
			AC_TIME = Accepted,
			Total = int( 100*Accepted/ZJTotal ),
			User = Name,
			Theme = T
		) , mimetype='image/svg+xml' )

	else: # user not found 
		return app.response_class( render_template("404.svg" , Theme = T) , mimetype='image/svg+xml' )



if __name__  ==  '__main__' :

	app.run( port=5000 )
	
	

	
    
    
    
    
