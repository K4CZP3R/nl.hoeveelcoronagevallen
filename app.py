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
    return render_template("index.html", gevallen=rivmData.aantal_gevallen, laatste_update=laatste_update, kop=rivmData.laatste_kop)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80,debug=True)