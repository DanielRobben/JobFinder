# Selenium is used in Python for Automation 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

# this prevets the page from closeing out
chrome_options.add_experimental_option("detach", True)

# This is where our Chrome driver is 
driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)

# This is the the website we are pulling from 
driver.get('http://www.glassdoor.com/sitedirectory/city-jobs.htm')

# This is supposed to open the Chrome in a maximized page 
chrome_options.add_argument("--start-maximized")

# This is where we are are inputting our search references
driver.find_element_by_xpath("//*[@id='sc.keyword']").send_keys("Entry Level Programer")

# # This is where we are are inputting our search references
# driver.find_element_by_xpath("//*[@id='sc.location']").send_keys("Burbank, CA")

# This is where we are clinking the Search Button 
driver.find_element_by_xpath("//*[@id='HeroSearchButton']").click()

# This is where we are seaching for our Job search elements 
jobs_list = driver.find_elements_by_xpath("//ul[@class='jlGrid hover']/li")
print(jobs_list)

# Keyword search 
keywords = ["python", "data analyst"]

# This is where we are Outputting our data into a Text file 
jobs_outfile = open('./jobs.txt', 'w')

for job in jobs_list:
    jobs_outfile.write(job.text)

# This is where we are closing our code 
jobs_outfile.close()

driver.close()

