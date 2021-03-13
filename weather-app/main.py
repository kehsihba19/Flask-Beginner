import requests
from flask import Flask ,render_template, request 

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
	new_city = request.form.get('city')
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8a60f97907057f9ec1f2cb3697be4c37'
	r = requests.get(url.format(new_city)).json()
	temp=(int(r['main']['temp'])-32)*(5/9)
	temp=float("{:.2f}".format(temp))
	weather = {'city' : new_city,'temperature' : temp,'description' : r['weather'][0]['description'],'icon' : r['weather'][0]['icon']}
	return render_template('index.html',weather=weather)

app.run()

