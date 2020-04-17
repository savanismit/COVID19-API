from flask import Flask,request 
import requests
import json

app = Flask(__name__) 
@app.route('/')
def test1():
    return "Hello!"

@app.route('/<string:msg>',methods=['GET','POST'])
def test(msg):   
    url = "https://covid-193.p.rapidapi.com/statistics"
    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "57bf763c17mshfe24b1073f868e8p1ab7b7jsnee514328dd7d"
    }

    response = requests.request("GET", url, headers=headers)
    data=response.text
    data=json.loads(data)
    for i in range(len(data["response"])):
        d = data["response"][i]["country"]
        if(d.lower()==msg.lower()):
            total=data["response"][i]["cases"]["total"]
            active_cases=data["response"][i]["cases"]["active"]
            recovered=data["response"][i]["cases"]["recovered"]
            critical_cases=data["response"][i]["cases"]["critical"]
            new_cases=data["response"][i]["cases"]["new"]
            total_deaths=data["response"][i]["deaths"]["total"]
            new_deaths=data["response"][i]["deaths"]["new"]
            time = data["response"][i]["time"]
            date = data["response"][i]["day"]
        
            result = {"country":msg,"total_cases":total,"active_cases":active_cases,"deaths":total_deaths,"new_cases":new_cases,"newdeaths":new_deaths,"recovered":recovered,"date":date,"time":time,"critical_cases":critical_cases,} 
            return(result)
    return("Enter a valid country name!")

if __name__ == '__main__':
	app.run(debug=True)