from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from api import get_bird_names 
from menu import print_menu
import time
# from menu import print_menu
import random
options = Options()
options.headless = True

browser = webdriver.Firefox(options=options)
url = 'https://uk.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck=domainnamehellothere.com'
name_list = get_bird_names()

while True:
	print("----------------------------------")
	print("SEARCHING...")
	print("----------------------------------")

	n = random.randint(0,len(name_list) -1)
	domain_name = name_list[n]

	url = 'https://uk.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck=' + domain_name + ".com"

	browser.get(url)
	time.sleep(2)
	available = ''
	try:
		available = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div[1]').text
	except:
		pass
	available = available.split(' ')[1].split('\n')[0]
	print(available)
	if available == 'Available' or available ==  'Domain':
		print(domain_name + ".com" + " is available!")
		print_menu()
		user_input = input(": ").rstrip()
		while True:
			try: 
				user_input = int(user_input)
				break
			except:
				user_input = input(": ").rstrip()
				continue
		if user_input == 1:
			# implement stuff
			new_browser = webdriver.Firefox()
			new_browser.get(url)
			break
		if user_input == 2:
			# implement stuff
			pass
		if user_input == 3:
			# implement stuff
			break
	else:
		print(domain_name + ".com" + " is taken!")
		continue