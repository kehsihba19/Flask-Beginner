import requests
from flask import Flask ,render_template,request

app = Flask(__name__)
@app.route("/",methods=['GET', 'POST'])
def home():
	if request.method == "POST":
		number = request.form["number"]
		url = "https://ajith-indian-mob-info.p.rapidapi.com/employees"
		querystring = {"mobno":number}
		headers = {
		    'x-rapidapi-host': "ajith-indian-mob-info.p.rapidapi.com",
		    'x-rapidapi-key': "a1fb61dabbmsh42f8db20975c1e2p136118jsn1d53864f487b"
		    }
		response = requests.get(url, headers=headers, params=querystring)
		a=response.json()
		val={'num':a["Number"],'state':a["State"],'provider':a["Provider"].split(" ")[0],'service':a["Service"]}
		return render_template('info.html',val=val)
	else:
		return render_template('index.html')


@app.route("/contact",methods=['GET', 'POST'])
def contact():
	if request.method == "POST":
		return render_template('index.html')
	else:
		return render_template('contact.html')

@app.route("/about")
def about():
	return render_template('about.html')


app.run(debug=True)