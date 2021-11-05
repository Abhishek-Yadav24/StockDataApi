# abhi24yadav02@gmail.com
# Abhishek@76666
# Abhishek-Yadav24

from flask import Flask,jsonify
from nsepy import get_history
import pandas as pd
from datetime import datetime,timedelta
app=Flask(__name__)

@app.route('/stockdata',method=['POST'])
def fetchdata(company):
    enddate = datetime.today()
    startdate = datetime.today()-timedelta(20)
    data=get_history(company['ticker'],start=startdate,end=enddate)
    print(data)
    print(type(data))
    data=data.to_dict('records')
    return jsonify(data)


@app.route('/<name>/<rollno>')
def name(name,rollno):
    return jsonify({"name": name,"rollno": rollno})

if __name__ == '__main__':

    app.run(debug=True)

