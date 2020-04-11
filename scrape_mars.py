# Dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
import pandas as pd

def scrape():

    ## SCRAPE MARS.NASA.GOV FOR MOST RECENT ARTILCE INFO ##
    # ----------------------------------------------------#

    # Scrape the url provided
    url = 'https://mars.nasa.gov/news/'
    response = requests.get(url)

    # Parse the webpage's html
    soup = bs(response.text, 'html.parser')

    # Extract Title and Description of first article from html
    news_title = soup.find(class_='content_title').text.strip()
    news_p = soup.find(class_='rollover_description_inner').text.strip()

    ## SCRAPE JPL.NASA.GOV IMAGES FOR FEATURED MARS IMAGE ##
    #------------------------------------------------------#
    # * Note - Unlike in the Jupyter notebook, I use requests.get rather 
    #   than Splinter here in the .py script so that the code won't try 
    #   to run before the browser opens and gets to the webpage. *

    # Scrape the url provided
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    response = requests.get(url)

    # Parse the webpage's html
    soup = bs(response.text, 'html.parser')

    # Identify the footer of the html and the elements within it
    image_url = soup.footer.a.get('data-fancybox-href')

    featured_image_url = 'https://www.jpl.nasa.gov' + image_url

    ## SCRAPE TWITTER.COM FOR LATEST MARS WEATHER TWEET ##
    #---------------------------------------------------#

    # Scrape the url provided
    url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(url)

    # Parse the webpage's html
    soup = bs(response.text, 'html.parser')

    # Used print(soup.prettify()) to observe html

   # Identify necessary html to pull data from and remove unnecessary ending text
    mars_weather = (soup.find(class_='js-tweet-text-container').p.text.strip())[:-30]

    ## SCRAPE SPACE-FACTS.COM FOR MARS FACTS TABLE ##
    #-----------------------------------------------#

# Convert Mars Data Table to html

    # Scrape the url provided
    url = 'https://space-facts.com/mars/'

    # Use Panda's `read_html` to parse the url
    table = pd.read_html(url)

    # After observing all tables resulting from above call,
    # we found that the third table was the one we wanted (table[2])
    table = table[2]

    # Reset Index and delete extra row it creates, then rename columns, and display
    table.set_index(table[0], inplace=True)
    del table[0]
    table.index.name = ''
    table.columns = ['Value']

    #render dataframe as html
    html = table.to_html()

    #write html to file
    text_file = open("table.html", "w")
    text_file.write(html)
    text_file.close()

    ## SCRAPE ASTROGEOLOGY.US.GOV FOR MARS PHOTOS ##
    #----------------------------------------------#

    # Scrape the url provided
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    response = requests.get(url)

    # Parse the webpage's html
    soup = bs(response.text, 'html.parser')

    # Scrape for element for each link to Mars images
    links = soup.find_all(class_='itemLink product-item')

    links_list = []

    for link in links:
        img = 'https://astrogeology.usgs.gov/' + link.get('href')
        links_list.append(img)
        
    # Scrape links found above for titles and links to final images
    hrefs = []
    titles = []

    for link in links_list:
        response = requests.get(link)
        soup = bs(response.text, 'html.parser')
        
        image = soup.find('a', href=True, text='Original')
        href = image['href']
        
        # Titles were stored as, for example, 'Cerberus Hemisphere Enhanced' so once
        # we scraped them, we removed the last part with the .replace() function
        title = soup.find(class_='title').text.strip().replace(' Enhanced','')
        
        titles.append(title)
        hrefs.append(href)

    # Create list of dictionaries containing titles and links to each related full res image

    hemisphere_image_urls = []

    for i in range(4):
        hem = {'title': titles[i], 'img_url': hrefs[i]}
        hemisphere_image_urls.append(hem)

    ## STORE ALL SCRAPED DATA INTO A DICTIONARY ##
    #--------------------------------------------#

    mars_data = {
        'news_title': news_title,
        'news_p': news_p,
        'featured_image_url': featured_image_url,
        'mars_weather': mars_weather,
        'html_table': html,
        'hemisphere_image_urls': hemisphere_image_urls
    }

    return mars_data