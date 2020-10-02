from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle
from time import sleep
from getpass import getpass
import schedule
import csv

username = input('Enter your facebook username \n')
password = getpass()
print('publishing ...')
url = "https://mbasic.facebook.com/"
options = Options()
options.headless = True
driver = webdriver.Chrome('../../chromedriver', options = options)

i = 0

def job():	
	global i
	driver.get(url)
	try:
		cookies = pickle.load(open('cookies.pkl', 'rb'))
		for cookie in cookies:
			driver.add_cookie(cookie)
	except Exception as e:
		print("There is no cookies, we will login.")
	driver.get(url)
	sleep(2)
	if driver.title == "Facebook – log in or sign up":
		usernameInput = driver.find_element_by_xpath("//input[@name='email']")
		passwordInput = driver.find_element_by_xpath("//input[@name='pass']")
		usernameInput.send_keys(username)
		passwordInput.send_keys(password)
		passwordInput.submit()
		cookies = driver.get_cookies()
		sleep(2)
		pickle.dump(cookies, open('cookies.pkl', "wb"))
		try:
			driver.find_element_by_xpath("//input[@value='OK']").click()
			sleep(1)
		except Exception as e:
			pass
		i = i + 1

	driver.find_element_by_xpath("//input[@value='Photo']").click()
	with open('data.csv', "r") as csvfile:
		reader = csv.DictReader(csvfile)
		rows = [r for r in reader]
	driver.find_element_by_xpath("//input[@name='file1']").send_keys(rows[i]['image'])
	driver.find_element_by_xpath("//input[@name='add_photo_done']").click()
	sleep(1)
	driver.find_element_by_xpath("//textarea[@name='xc_message']").send_keys(rows[i]['text'])
	driver.find_element_by_xpath("//input[@name='view_post']").click()
	print("Post published !")

schedule.every().day.at("10:30").do(job)
  
while True:
	schedule.run_pending()
	sleep(1)
