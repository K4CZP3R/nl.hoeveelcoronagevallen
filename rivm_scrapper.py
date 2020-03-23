import requests, bs4
from time import sleep, time
import CoronaDb, RivmData


def get_rivm_covid():
    res = requests.get("https://www.rivm.nl/nieuws/actuele-informatie-over-coronavirus").text
    soup = bs4.BeautifulSoup(res, features="html.parser")

    gevallen = soup.select_one("td h2").text
    laatste_kop = soup.select_one("h2:nth-of-type(2)").text
    return [gevallen, laatste_kop]

cdb = CoronaDb.CoronaDb()


last_check = 0
check_every_s = 60*60
while True:
    if int(time()) - last_check > check_every_s:
        last_check = int(time())

        scrapper = get_rivm_covid()

        actual_corona_gevallen = scrapper[0]
        actual_corona_kop = scrapper[1]
        actual_corona_time = int(time())
        print(f"Corona update! Gevallen: {actual_corona_gevallen} at time={actual_corona_time} with kop={actual_corona_kop}")
        try:
            actual_corona_gevallen = int(actual_corona_gevallen)
        except ValueError:
            print("INVALID CORONA GEVALLEN!")
            continue
        r_data = RivmData.RivmData(actual_corona_time, actual_corona_gevallen, actual_corona_kop)
        cdb.add_data(r_data)
    