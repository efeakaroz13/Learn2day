# Learn2day
A web application which helps people to learn English with wikipedia articles and images!
# API
To use it with other programming languages and mobile apps, you can run `scraper.py` on a server with flask. But don't forget to use `flask-cors`.
### Note
I will write a code to make a server with it soon!
# Tech behind the project
## Python Side
I used  `python flask` to render an html template on browser;  `requests` for retrieving html from external links and  `BeautifulSoup4` for scraping the html page.
## C++ Side
Program is getting wikipedia summaries with C++. I used `nlohmann/json` for parsing json which program gets with `curl`.

