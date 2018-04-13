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


def wwo_search(date):

    base_url = "https://api.worldweatheronline.com/premium/v1/past-weather.ashx"
    location = "Ann+Arbor,MI"
    url = base_url + "?q=" + location + "&key=" + WWO_API + "&date=" + date + "&format=json"
    print(url)
    if url in CACHE_DICTION:
        try:
            # print("getting cache")
            min_temp_f = CACHE_DICTION[url]["data"]["weather"][0]["mintempF"]
            max_temp_f = CACHE_DICTION[url]["data"]["weather"][0]["maxtempF"]
        except:
            print("cache error")

    else:
        try:
            print("making request to wwo")
            results = requests.get(url).text
            results_dict = json.loads(results)

            min_temp_f = results_dict["data"]["weather"][0]["mintempF"]
            max_temp_f = results_dict["data"]["weather"][0]["maxtempF"]

            CACHE_DICTION[url] = results_dict
            dumped_json_cache = json.dumps(CACHE_DICTION)
            fw = open(CACHE_FNAME,"w")
            fw.write(dumped_json_cache)
            fw.close() 

        except:
            print("Failed:", date)

    formatted_location = location.replace("+", " ")
    formatted_location = formatted_location.replace(",", ", ")

    try:
        print(date, formatted_location, "Min:", min_temp_f, "Max:", max_temp_f)
    except:
        print("no data")


for a in range(17608,17609):
    wwo_search(CACHE_DICTION["dates"][a])





