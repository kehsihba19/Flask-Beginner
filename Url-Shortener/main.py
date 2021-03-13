from flask import Flask, render_template, request, redirect, url_for
import requests
import pyshorteners

app = Flask(__name__) 
@app.route('/',methods=['GET','POST'])
def home():
	if request.method == "POST":
		url = request.form["url"]
		s = pyshorteners.Shortener()
		shorten=(s.tinyurl.short(url))
		print(shorten)
		return render_template('shorten.html',url=shorten)
	else:
		return render_template('home.html')

@app.route("/contact")
def contact():
	return render_template('contact.html')

@app.route("/about")
def about():
	return render_template('about.html')


app.run(debug = True) 