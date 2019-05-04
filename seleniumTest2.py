###############################
#Claroty Automation Assignment#
#########Shahar Sadeh##########
###############################

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

#open Chrome web driver
driver = webdriver.Chrome()
driver.get("https://www.google.com/en")


#enter search key 'Claroty'
try:
	input_element = driver.find_element_by_name("q")
except NoSuchElementException:
	print("Could not find google's search field element!\nExiting...")
	quit()
	
input_element.send_keys("Claroty")
input_element.submit()

#find the number of results and print it to console
try:
	results_element = driver.find_element_by_id("resultStats")
except NoSuchElementException:
	print("Could not get the number of results element!\nExiting...")
	quit()
	
results_str = results_element.text.split()[1]
numOfResults = int(results_str.replace(',', ''))

print("\nNumber of results for keyword 'Claroty' is: ", numOfResults)


#retrieve all the results URLs of the first  page, then verify that the first result is 'www.claroty.com'
try:
	urls = driver.find_elements_by_xpath("//div[@class='g']//a")
except NoSuchElementException:
	print("Could not retrieve URL result elements!\nExiting...")
	quit()
	
first_url = urls[0].get_attribute("href")

if "www.claroty.com" in first_url:
	print("\nFirst result is claroty.com!")
else:
	print("\nFirst result is not claroty.com!")
	
	
#enter Claroty careers web page and print the number of displayed careers
driver.get("https://www.claroty.com/careers")

try:
	careers = driver.find_elements_by_xpath("//div[@class='w-dyn-item']")
except NoSuchElementException:
	print("Could not get Claroty career elements!\nExiting...")
	quit()
	
print("\nNumber of job opportunities at Claroty is:", len(careers))


driver.quit()
print("\nEnd of test")
 