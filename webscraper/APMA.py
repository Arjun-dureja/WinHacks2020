#apt-get install python3-bs4
#pip3 install lxml

import requests, csv, string, time
from bs4 import BeautifulSoup
import pymongo
from pymongo import MongoClient
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

client = pymongo.MongoClient("mongodb+srv://uzair:winhacks@winhacks-e12bb.mongodb.net/test?retryWrites=true&w=majority")
db = client.info
collection=db.inputs

URL = "http://apma.ca/members"

#Selenium Setup
driver = webdriver.Firefox()
driver.get(URL)

print("Loading Results")

while True:
    try:
        loadmore = driver.find_element_by_class_name("w2dc-show-more-button")
        time.sleep(0.5)
        loadmore.click()
        print("Load More Results...") 
        time.sleep(0.5)
    except ElementNotInteractableException:
        print("\nReached bottom of page")
        break

print("done")
print("Scraping Company Data From Loaded Website")

#BeautifulSoup Setup
soup = BeautifulSoup(driver.page_source, 'html.parser')

x = soup.find_all('div', class_="w2dc-listing-text-content-wrap-nologo")
for supplier in x:
    time.sleep(0.001)

    child = supplier.findChildren()
    CompanyName = supplier.find("header", class_="w2dc-listing-header")
    CompanyAddress = supplier.find("span", itemprop="streetAddress")
    CompanyTele = supplier.find("span", class_="w2dc-field-phone-content")

    name = "BLANK"
    address = "BLANK"
    tele = "BLANK"

    if CompanyName != None: name = CompanyName.get_text().translate(str.maketrans('', '', string.punctuation)).replace("\n", "")
    if CompanyAddress != None: address = CompanyAddress.get_text().translate(str.maketrans('', '', string.punctuation)).replace("\n", "")
    if CompanyTele != None: tele = CompanyTele.get_text().translate(str.maketrans('', '', string.punctuation)).replace("\n","")
    provider = "APMA"
    
    csvrow = [provider, name,address,tele]
    dictrow = {'provider':provider, 'name': name, 'address':address, 'telephone':tele}

    print (name, address, tele)
    with open('APMA.csv', mode='a') as apma:
        apma_writer = csv.writer(apma, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        apma_writer.writerow([name,address,tele])
    
    result=collection.insert_one(dictrow)
    print('Added {0} to Database'.format(result.inserted_id))

print("Done!")