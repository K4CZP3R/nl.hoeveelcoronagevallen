from flask import Flask, render_template
from CoronaDb import CoronaDb
from RivmData import RivmData
from datetime import datetime

app = Flask(__name__)
cdb = CoronaDb()



@app.route("/")
def index():
    rivmData = cdb.get_data()
    rivmData: RivmData
    laatste_update = datetime.fromtimestamp(rivmData.unix_time).strftime("%d.%m.%Y %H:%M:%S")

    rivmDaysData = cdb.get_days_data()
    print(rivmDaysData.values())
    data_keys = list(rivmDaysData.keys())
    data_values = list(rivmDaysData.values())


    data_to_show = list()
    for i in range(0, len(data_keys)):
        
        if(i+1 < len(data_keys)):
            delta = data_values[i].aantal_gevallen - data_values[i+1].aantal_gevallen
        else:
            delta = 0

        data_to_show.append([i, data_keys[i], data_values[i].aantal_gevallen, delta])
    return render_template("index.html", gevallen=rivmData.aantal_gevallen, laatste_update=laatste_update, kop=rivmData.laatste_kop, days_data=data_to_show)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80,debug=True)