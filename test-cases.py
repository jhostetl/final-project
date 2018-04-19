import unittest
import json
from bs4 import BeautifulSoup

class DayTemp():
    def __init__(self, day, low, high):
        self.day = day
        self.low = low
        self.high = high
    def __str__(self):
        return 'The high on {} was {} and the low was {}'.format(self.day, int(self.high), int(self.low)) 

CACHE_FNAME = 'scraping_cache_dict.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {}

class Testing(unittest.TestCase):

    def testWunderground(self):

        # ann arbor weather in january 2017
        url = "https://www.wunderground.com/history/airport/KARB/2017/1/1/MonthlyCalendar.html"
        monthly_list = CACHE_DICTION[url]
        january_length = len(monthly_list)
        january_1 = DayTemp("January 1, 2017", float(CACHE_DICTION[url][0]["low"]), float(CACHE_DICTION[url][0]["high"]))

        january_31_low = float(CACHE_DICTION[url][30]["low"])
        january_31_high = float(CACHE_DICTION[url][30]["high"])
 
        days = 0
        for i in range(1,13):
            url = "https://www.wunderground.com/history/airport/KARB/2017/" + str(i) + "/1/MonthlyCalendar.html"
            monthly_list = CACHE_DICTION[url]
            days += len(monthly_list)

        self.assertEqual(january_length, 31)
        self.assertEqual(january_1.low, 16)
        self.assertEqual(january_1.high, 37)
        self.assertEqual(january_1.__str__(), "The high on January 1, 2017 was 37 and the low was 16")       
        self.assertEqual(january_31_low, 24)
        self.assertEqual(january_31_high, 34)
        self.assertEqual(days, 365)

        url = "https://www.wunderground.com/history/airport/KARB/2017/12/1/MonthlyCalendar.html"
        monthly_list = CACHE_DICTION[url]
        dec_31_low = float(CACHE_DICTION[url][30]["low"])
        dec_31_high = float(CACHE_DICTION[url][30]["high"])

        self.assertEqual(dec_31_low, -6)
        self.assertEqual(dec_31_high, 15)

        url = "https://www.wunderground.com/history/airport/KSEA/2017/12/1/MonthlyCalendar.html"
        monthly_list = CACHE_DICTION[url]
        dec_31_low = float(CACHE_DICTION[url][30]["low"])
        dec_31_high = float(CACHE_DICTION[url][30]["high"])

        self.assertEqual(dec_31_low, 33)
        self.assertEqual(dec_31_high, 43)        

    def testWundergroundAverages(self):
        total = 0
        counter = 0
        for i in range(2001,2017):
            url = "https://www.wunderground.com/history/airport/KARB/" + str(i) + "/1/1/MonthlyCalendar.html"
            if url in CACHE_DICTION:
                low = CACHE_DICTION[url][0]["low"]
                total += float(low)
                counter += 1
        average = round(total/counter)
        self.assertEqual(average, 18)   

        total = 0
        counter = 0
        for i in range(2001,2017):
            url = "https://www.wunderground.com/history/airport/KARB/" + str(i) + "/1/1/MonthlyCalendar.html"
            if url in CACHE_DICTION:
                low = CACHE_DICTION[url][30]["high"]
                total += float(low)
                counter += 1
        average = round(total/counter)
        self.assertEqual(average, 31) 

        total = 0
        counter = 0
        for i in range(2001,2017):
            url = "https://www.wunderground.com/history/airport/KLAS/" + str(i) + "/7/1/MonthlyCalendar.html"
            if url in CACHE_DICTION:
                low = CACHE_DICTION[url][3]["high"]
                total += float(low)
                counter += 1
        average = round(total/counter)
        self.assertEqual(average, 104) 

    def testingExtremes(self):
        low_list = []
        for i in range(1,13):
            url = "https://www.wunderground.com/history/airport/KARB/2017/" + str(i) + "/1/MonthlyCalendar.html"
            counter = 0
            for day in CACHE_DICTION[url]:
                low = float(CACHE_DICTION[url][counter]["low"])
                low_list.append(low)
                counter += 1
        lowest = sorted(low_list)[0]
        self.assertEqual(lowest, -18) 

        high_list = []
        for i in range(1,13):
            url = "https://www.wunderground.com/history/airport/KARB/2017/" + str(i) + "/1/MonthlyCalendar.html"
            counter = 0
            for day in CACHE_DICTION[url]:
                high = float(CACHE_DICTION[url][counter]["high"])
                high_list.append(high)
                counter += 1
        highest = sorted(high_list)[-1]
        self.assertEqual(highest, 93)

unittest.main(verbosity=2)


