from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set path to chromedriver as per your configuration
webdriver_service = Service("/Users/emrecanduygulu/Downloads/chromedriver-mac-arm64/chromedriver")  # Change this to the correct path

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Open LinkedIn job search page
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3920627800&geoId=103035651&keywords=Working%20Student&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")

# Allow some time for the page to load
time.sleep(5)  # Adjust the sleep time as needed

# Parse the page source with BeautifulSoup
html_text = driver.page_source
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='ember-view jobs-search-results__list-item occludable-update p0 relative scaffold-layout__list-item')

# Print out the job titles
for job in jobs:
    job_title = job.find('span', class_='screen-reader-text').get_text(strip=True)
    print(job_title)

# Close the browser
driver.quit()