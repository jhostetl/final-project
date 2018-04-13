I created WeatherComplainer.com for this project. It takes historical data and compares it to the current temperature. It then tells you whether you can complain about the weather. 

Data was scraped from Wunderground for the historical data. This will be replaced with NOAA data when I update the website at a future point. An API call is made to WorldWeatherOnline.com to get the current forecast. This is then stored in a MySql table so that it only needs to be requested once.

I also used the APIs for NOAA.gov and WeatherBit.io but they weren't included in the website data.

wunderground-scraping.py starts with a list of airport codes. Then I loop through the airports, using Beautiful Soup to scrape data for the high and low temperatures from the years 2000-2017 at these locations. This data is cached in scraping_cache_dict.json. I then initialize a database and insert the cached data into a sqllite database. 

It was interesting to find a few errors in the data that I used. I put up a page with extreme temperatures, https://www.weathercomplainer.com/extremes It's obvious that it has never been 129 degrees in Seattle or -25 in San Francisco. However, Wunderground shows this. I'm curious how many less obvious errors exist in the data.