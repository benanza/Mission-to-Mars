# Mission-to-Mars

*Note: must be running Flask app locally for webpage to function*

*See https://github.com/benanza/Mission-to-Mars/tree/master/Screenshots for page screenshots*

### The Project: Build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page

-----

#### Complete initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter:

1. Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text

2. Use splinter to navigate the JPL Mars Space Images

3. Visit the Mars Weather twitter account and scrape the latest Mars weather tweet from the page

4. Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc., then convert the data to a HTML table string.

5. Visit the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.

#### Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

1. Convert Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of scraping code from above and return one Python dictionary containing all of the scraped data.

2. Create a route called /scrape that will import your scrape_mars.py script and call your scrape function. Store the return value in Mongo as a Python dictionary.

3. Create a root route / that will query Mongo database and pass the mars data into an HTML template to display the data.

4. A template HTML file called index.html will take the mars data dictionary and display all of the data in the appropriate HTML elements.
