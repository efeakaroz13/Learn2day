# Learn2day
A web application which helps people to learn English with wikipedia articles and images!
### Note
I will write a code to make a server with it soon!
# Tech behind the project
## Python Side
I used  `python flask` to render an html template on browser;  `requests` for retrieving html from external links and  `BeautifulSoup4` for scraping the html page.
## C++ Side
Program is getting wikipedia summaries with C++. I used `nlohmann/json` for parsing json which program gets with `curl`.

# Documentation for API
This is the official Learn2day documentation. The API endpoint is at `/api` but unfortunatly we haven't got a server running with this code. You can use the code for creating a server! 
## API Arguments and Usage
`lang`: you can specify the language for translating the english word
note: `lang` makes the API slower because it translates the wikipedia summary and the word. For faster results use without `lang` argument


