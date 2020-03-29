import requests, csv, string, time
from bs4 import BeautifulSoup
import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://uzair:winhacks@winhacks-e12bb.mongodb.net/test?retryWrites=true&w=majority")
db = client.info
collection=db.inputs

soup = BeautifulSoup(open("Members Directory | APMA Members Directory.html"), "html.parser")

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

    with open('APMA.csv', mode='a') as apma:
        apma_writer = csv.writer(apma, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        apma_writer.writerow(csvrow)
    
    result=collection.insert_one(dictrow)
    print('One post: {0}'.format(result.inserted_id))
    
