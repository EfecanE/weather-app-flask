from flask import Flask,render_template,url_for,redirect,request
import requests
import json


app = Flask(__name__)
@app.route("/",methods=["POST","GET"])
def index():
    if request.method == "POST":
        cityName = request.form.get("city")
        
        url = "https://community-open-weather-map.p.rapidapi.com/weather"

        querystring = {"q":{},"lat":"0","lon":"0","id":"2172797","lang":"null","units":"metric"}
        querystring["q"] = cityName
        
        headers = {
            "X-RapidAPI-Key": "97f2822611msh8c3c413a3dc2263p1c515fjsn3d2df0210c04",
            "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        convertedText = json.loads(response.text)
        
        weatherdict = {
            'city' : convertedText["name"],
            'temperature' : convertedText["main"]["temp"],
            'description' : convertedText["weather"][0]["description"],
            'icon' : convertedText["weather"][0]["icon"]
        }
    

        return render_template("index.html", weatherdict = weatherdict)
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)