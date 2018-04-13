import requests
import json



CACHE_FNAME = 'cache_dict.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {}


def weatherbit_api(from_date, to_date):
    
    url = "https://api.weatherbit.io/v2.0/history/daily?city=Ann+Arbor,MI&start_date=" + from_date + "&end_date=" + to_date + "&key=" + WEATHERBIT_API

    if url in CACHE_DICTION:
        try:
            pass
            # print("getting cache")
        except:
            pass
            # print("cache error")

    else:
        try:
            print("making request to weather bit")
            results = requests.get(url).text
            results_dict = json.loads(results)

            CACHE_DICTION[url] = results_dict
            dumped_json_cache = json.dumps(CACHE_DICTION)
            fw = open(CACHE_FNAME,"w")
            fw.write(dumped_json_cache)
            fw.close() 

        except:
            print("Failed:", date)

    try:
        min_temp = CACHE_DICTION[url]["data"][0]["min_temp"]
        max_temp = CACHE_DICTION[url]["data"][0]["max_temp"]
        print(from_date, "Min:", min_temp, "Max:", max_temp)
    except:
        print("no data to show")    

def date_formatter(year,month,day):
    if month < 10:
        month = "0" + str(month)
    if day < 10:
        day = "0" + str(day)

    date_string = str(year) + "-" + str(month) + "-" + str(day)
    return date_string

# jan 1, 2017 start = 17155

for a in range(17550,17610):
    weatherbit_api(CACHE_DICTION["dates"][a],CACHE_DICTION["dates"][a + 1])












