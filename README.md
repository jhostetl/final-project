I created WeatherComplainer.com for this project. It takes historical data and compares it to the current temperature. It then tells you whether you can complain about the weather. There have been a lot of days to complain about this month. 

Data was scraped from Wunderground for the historical data. This will be replaced with NOAA data when I update the website at a future point. An API call is made to WorldWeatherOnline.com to get the current forecast. This is then stored in a MySql table so that it only needs to be requested once.

I also used the APIs for NOAA.gov and WeatherBit.io but they weren't included in the website data. To run weatherbit-apy.py and wwo-api.py you would need an API key. 

wunderground-scraping.py starts with a list of airport codes. Then I loop through the airports, using Beautiful Soup to scrape data for the high and low temperatures for each day from the years 2000-2017 at these locations. This data is cached in scraping_cache_dict.json. I then initialize a database and insert the cached data into a sqllite database. The sqllite database is then converted to a MySql database for use with php on the web.

I used a class in the test-cases.py file and a join in the php file of the homepage of WeatherComplainer.com. I found that joins would slow down the sql query, so I mostly joined the data ahead of time into a new table. This page uses joins and take several seconds to load, https://www.weathercomplainer.com/today The data on this page was joined ahead of time and loads immediately, https://www.weathercomplainer.com/extremes

It was interesting to find a few errors in the data that I used. I put up a page with extreme temperatures, https://www.weathercomplainer.com/extremes It's obvious that it has never been 129 degrees in Seattle or -25 in San Francisco. However, Wunderground shows this. 